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
            <div>
                <p>{restaurant.name}</p>
            </div>
            <div className='order-details'>
                <p>{orderData.items} items - ${orderData.totalCost}</p>
                <p>Deliver to {orderData.address}</p>
            </div>
        </div>
    )
}

export default OrderTile