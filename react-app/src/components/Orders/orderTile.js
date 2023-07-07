import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

const OrderTile = ({ orderData }) => {
    const [restaurant, setRestaurant] = useState({})

    const getRestaurantInfo = async () => {
        const res = await fetch(`/api/restaurants/${orderData.restaurantId}`)

        const data = await res.json()

        setRestaurant(data.restaurant_info)
    }

    useEffect(() => {
        getRestaurantInfo()
    }, [])

    if (!restaurant) return null
    // console.log(restaurant)
    return (
        <div className='order-tile'>
            <img src={restaurant.imageUrl}/>
            <div>
                <div>
                    <h3>{restaurant.name}</h3>
                    <p>{orderData.totalItems} items for {orderData.totalCost} · {orderData.orderedAt} · View receipt</p>
                    <ul>
                        {Object.values(orderData.Items).map(item => (
                            <li key={item.id}>
                                <div>{item.quantity}</div>
                                <div>
                                    <h4>{item.name}</h4>
                                    <p>{item.description}</p>
                                </div>
                            </li>
                        ))}
                    </ul>
                </div>
                <button>View Store</button>
            </div>
        </div>
    )
}

export default OrderTile
