import React, { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { addToCartThunk } from "../../store/ordersReducer";

import './itemModal.css'

const ItemModal = ({ menuItem }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    let [quantity, setQuantity] = useState(1)
    let [price, setPrice] = useState(menuItem.price * quantity)
    const [showMenu, setShowMenu] = useState(false)
    const modalRef = useRef()
    const order = useSelector(state => state.orders.cart)

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

    const openMenu = () => {
      if (showMenu) return;
      setShowMenu(true);
  };

    const closeMenu = () => setShowMenu(false);

    const incrementQuantity = () => {
      setQuantity(quantity += 1)
    }
    
    const decrementQuantity = () => {
      setQuantity(quantity -= 1)
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log("order id ",order.id, "menu item id ", menuItem.id, "quantity ", quantity)
        const data = await dispatch(addToCartThunk(order.id, menuItem.id, quantity));

        closeMenu();
    }

    const modalClassName = "add-item-modal" + (showMenu ? "" : " hidden");

    return (
        <>
        <h1 onClick={openMenu} className="plus">+</h1>
        <div className={modalClassName} ref={modalRef}>
            <button><i onClick={closeMenu} class="fa-solid fa-x"></i></button>
            <div className="add-to-cart-modal-details">
                <h2>{menuItem.name}</h2>
                <img className="itemImage" src={menuItem.imageUrl} alt="image"/>
                <div className="edit-quantity-div">
                  <button onClick={decrementQuantity}>-</button>
                  <h4>{quantity}</h4>
                  <button onClick={incrementQuantity}>+</button>
                </div>
                <button onClick={handleSubmit}>Add to cart - ${price}</button>
            </div>
        </div>
        </>
    )
}

export default ItemModal;