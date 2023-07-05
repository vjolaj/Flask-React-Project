import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getUserOrdersThunk } from '../../store/ordersReducer';
import OrderTile from './orderTile';


const PastOrdersPage = () => {
    const dispatch = useDispatch();
    const orders = useSelector(state => state.orders.currentUserOrders);

    useEffect(() => {
        dispatch(getUserOrdersThunk())
    }, [dispatch])

    console.log(orders)

    return (
        <div className="past-orders-div">
            <h2>Past Orders</h2>
            <ul id="orders-list">
                {Object.values(orders).map(order => (
                    <li key={order.id}>
                        <OrderTile orderData={order} />
                    </li>
                ))}
            </ul>
        </div>
    )
};

export default PastOrdersPage