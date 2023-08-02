import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getUserOrdersThunk } from "../../store/ordersReducer";
import OrderTile from "./orderTile";
import "./PastOrders.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

const PastOrdersPage = () => {
  const dispatch = useDispatch();
  const orders = useSelector((state) => state.orders.currentUserOrders);

  useEffect(() => {
    dispatch(getUserOrdersThunk());
  }, [dispatch]);

  return (
    <div className="past-orders-div">
      
      {Object.values(orders).length === 0 ? (
        <div className="no-orders">
            <h2>Past Orders</h2>
          <p>You haven't placed any orders yet
          </p>
          <NavLink exact to="/restaurants" >
            <p>Click here to start shopping</p>
          </NavLink>
          
        </div>
      ) : (
        <div> 
        <h1>Past Orders</h1>
        <ul id="orders-list">
          {Object.values(orders)
            .map((order) => (
                
              <li key={order.id}>
                <OrderTile orderData={order} />
              </li>
            ))
            .reverse()}
        </ul>
        </div>
      )}
    </div>
  );
};

export default PastOrdersPage;
