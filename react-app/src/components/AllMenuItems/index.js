/* eslint-disable jsx-a11y/img-redundant-alt */
import React, { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./AllMenuItems.css";
import { getAllMenuItemsThunk } from "../../store/menuItemsReducer";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import ItemModal from "./itemModal";

export default function RestaurantMenuItems() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const menuItems = useSelector((state) => state.menuItems.allMenuItems);
  const modalRef = useRef();

  const [showMenu, setShowMenu] = useState(false);

  const openMenu = (menuItem) => {
    if (showMenu) return;
        setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!modalRef.current || !modalRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const modalClassName = "item-modal" + (showMenu ? "" : " hidden")

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
            <div className="itemImageContainer">
           <img className="itemImage" src={menuItem.imageUrl} alt="image"/>
          {/* <ItemModal menuItem={menuItem} />   */}
            </div>
          
          <h3 className="itemName">{menuItem.itemName}</h3>
          <div className="itemName">${menuItem.price}</div>
          </div>
         
          
        </div>
      ))}
    </div>
  );
}
