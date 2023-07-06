import React, { useState, useRef, useEffect } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
// import { addToCartThunk } from "../../store/ordersReducer";


const ItemModal = ({ menuItem }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    let [quantity, setQuantity] = useState(1)
    let [price, setPrice] = useState(menuItem.price * quantity)
    const [showMenu, setShowMenu] = useState(false)
    const modalRef = useRef()

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

    const handleSubmit = async (e) => {
        e.preventDefault();
        // const data = await dispatch(addToCartThunk(menuItem));

        closeModal();
    }

    const modalClassName = "add-item-modal" + (showMenu ? "" : " hidden");

    return (
        <>
        <h1 className="plus">+</h1>
        <div className={modalClassName} ref={modalRef}>
            <button><i onClick={closeMenu} class="fa-solid fa-x"></i></button>
            <div className="add-to-cart-modal-details">
                <h2>{menuItem.name}</h2>
                <img className="itemImage" src={menuItem.imageUrl} alt="image"/>
                <span><button onClick={setQuantity(quantity--)}>-</button> {quantity} <button onClick={setQuantity(quantity++)}>+</button></span>
                <button onClick={handleSubmit}>Add to cart - ${price}</button>
            </div>
        </div>
        </>
    )
}

export default ItemModal;