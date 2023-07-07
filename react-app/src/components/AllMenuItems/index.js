/* eslint-disable jsx-a11y/img-redundant-alt */
import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./AllMenuItems.css";
import { getAllMenuItemsThunk } from "../../store/menuItemsReducer";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";

export default function RestaurantMenuItems() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const menuItems = useSelector((state) => state.menuItems.allMenuItems);


  useEffect(() => {
    dispatch(getAllMenuItemsThunk(restaurantId));
  }, [dispatch, restaurantId]);

  if (!menuItems) {
    return <div>Loading Menu Items...</div>;
  }
 
  return (
    <div className="menuItemsContainer">
      {Object.values(menuItems).map((menuItem) => (
        <div className="itemContainer" key={menuItem.id}>
          <div className="single-item-container">
            <div>
           <img className="itemImage" src={menuItem.imageUrl} alt="image"/>
           <div className="itemImageContainer">
             <h1 className="plus">+</h1> 
           </div>
          
            </div>
          
          <h3 className="itemName">{menuItem.itemName}</h3>
          <div className="itemName">${menuItem.price}</div>
          </div>
         
          
        </div>
      ))}
    </div>
  );
}
