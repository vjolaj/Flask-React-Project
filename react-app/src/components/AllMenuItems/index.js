import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import "./AllMenuItems.css";
import { getAllMenuItemsThunk } from "../../store/menuItemsReducer";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";

export default function RestaurantMenuItems() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const menuItems = useSelector((state) => state.menuItems.allMenuItems);
  console.log(menuItems);
  // const spot = useSelector((state) => state.spot.singleSpot);
  // const reviews = useSelector((state) => state.review.reviews);

  useEffect(() => {
    dispatch(getAllMenuItemsThunk(restaurantId));
  }, [dispatch]);

  if (!menuItems) {
    return <div>Loading Menu Items...</div>;
  }

  return (
    <div className="menuItemsContainer">
      {Object.values(menuItems).map((menuItem) => (
        <div className="itemContainer" key={menuItem.id}>
          <h2 className="itemName">{menuItem.itemName}</h2>
          <div>{menuItem.price}</div>
          {/* <div>{menuItem.description}</div> */}
          {/* <div>{menuItem.itemType}</div> */}
          <img className="itemImage" src={menuItem.imageUrl} alt="image of item" />
        </div>
      ))}
    </div>
  );
}
