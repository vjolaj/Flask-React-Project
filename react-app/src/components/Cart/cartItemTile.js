import React, { useState, useRef, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { deleteOrderItemThunk, getCartThunk, updateItemQuantityThunk } from "../../store/ordersReducer";

const CartItemTile = ({ itemData, orderId }) => {
    const dispatch = useDispatch()
    let [quantity, setQuantity] = useState(itemData.quantity)
    let [price, setPrice] = useState(itemData.price * quantity)
    console.log("this is your item data ", itemData)

    // useEffect(() => {
    //     dispatch(updateItemQuantityThunk(quantity, orderId, itemData.id))
    // }, [dispatch, quantity])

    const incrementQuantity = () => {
        setQuantity(quantity += 1)
        dispatch(updateItemQuantityThunk(quantity, orderId, itemData.id))
        dispatch(getCartThunk())
    }
      
    const decrementQuantity = () => {
        setQuantity(quantity -= 1)
        dispatch(updateItemQuantityThunk(quantity, orderId, itemData.id))
        dispatch(getCartThunk())
    }

    const deleteItem = () => {
        dispatch(deleteOrderItemThunk(orderId, itemData.id))
    }

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
                {quantity === 1 ?(
                    <button onClick={deleteItem}><i class="fa-solid fa-trash"></i></button>
                ): (<button onClick={decrementQuantity}>-</button>)}
                <p>{quantity}</p>
                <button onClick={incrementQuantity}>+</button>
            </div>
        </div>
      )
}

export default CartItemTile;