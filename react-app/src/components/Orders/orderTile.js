import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from "react-router-dom";
import './PastOrders.css'

const OrderTile = ({ orderData }) => {
    const [restaurant, setRestaurant] = useState({})
    const history = useHistory()

    const getRestaurantInfo = async () => {
        const res = await fetch(`/api/restaurants/${orderData.restaurantId}`)

        const data = await res.json()

        setRestaurant(data.restaurant_info)
    }

    const convertDate = (date) => {
        const newDate = new Date(date)
        const options = { day: 'numeric', month: 'long', year: 'numeric' };
        const convertedDate = newDate.toLocaleString('en-US', options);
        return convertedDate
    }


    useEffect(() => {
        getRestaurantInfo()
    }, [])

    if (!restaurant) return null
    return (
        <div className='order-tile'>
            <div>
                <img className='order-image' src={restaurant.imageUrl}/>
            </div>
            <div className='order-content'>
                <div className='order-info'>
                    <h3>{restaurant.name}</h3>
                    {orderData.totalItems === 1 ? (
                    <p>{orderData.totalItems} item for ${Number(orderData.totalPrice).toFixed(2)} · {convertDate(orderData.orderedAt)}</p>

                    ): (
                        <p>{orderData.totalItems} items for ${Number(orderData.totalPrice).toFixed(2)} · {convertDate(orderData.orderedAt)}</p>
                    )}
                    <ul>
                        {Object.values(orderData.Items).map(item => (
                            <li className='order-item-desc' key={item.id}>
                                <div className='order-item-quantity'>{item.quantity}</div>
                                <div>
                                    <h4>{item.itemName}</h4>
                                </div>
                            </li>
                        ))}
                    </ul>
                </div>
                <button onClick={() => history.push(`/restaurants/${restaurant.id}`)}>View Store</button>
            </div>
        </div>
    )
}

export default OrderTile
