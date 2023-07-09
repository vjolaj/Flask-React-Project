import React, { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { deleteOrderItemThunk, getCartThunk, updateItemQuantityThunk } from "../../store/ordersReducer";

const CheckoutItemTile = ({ itemData }) => {
    const dispatch = useDispatch()
    let quantity = useSelector(state => state.orders.cart.Items[itemData.id].quantity)
    let [price, setPrice] = useState(itemData.price * quantity)
    console.log("this is your item data ", itemData)

    return (
        <div className='cart-item-tile'>
            <div className="cart-item-tile-left">
            <div className='item-img-div'>
                <img className='cart-item-img' src={itemData.imageUrl} alt='image' />
            </div>
            <div className='cart-item-details'>
                <h6>{itemData.itemName}</h6>
                <p>${itemData.price}</p>
            </div>
            </div>
            <div className='cart-item-quantity'>
                <p>{quantity}</p>
            </div>
        </div>
      )
}

export default CheckoutItemTile;