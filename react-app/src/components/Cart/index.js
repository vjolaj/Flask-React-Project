import React, { useEffect, useState, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import { Link } from 'react-router-dom';
import CartItemTile from './cartItemTile';

import { getCartThunk, updateItemQuantityThunk } from '../../store/ordersReducer';
import './cart.css'

const Cart = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const modalRef = useRef();

    const cart = useSelector(state => state.orders.cart)
    const items = useSelector(state => state.orders.cart.Items)
    const [showMenu, setShowMenu] = useState(false);
    const openMenu = () => {
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
    }, [showMenu, items]);

    useEffect(() => {
        dispatch(updateItemQuantityThunk())
        dispatch(getCartThunk())
    }, [dispatch])

    const closeMenu = () => setShowMenu(false);

    const cartClassName = "cart-dropdown" + (showMenu ? "" : " hidden");
    return (
        <div className='cart-modal'>
            <div className='cart-button'>
                <button onClick={openMenu} className='cart-button'>
                <i class="fa-solid fa-cart-shopping"></i><p>{cart.totalItems} item{cart.totalItems === 1 ? "" : "s"}</p>
                </button>
            </div>
            <div className={cartClassName} ref={modalRef}>
                <button><i onClick={closeMenu} class="fa-solid fa-x"></i></button>
                {cart.Items ? <div className='cart-modal-details'>
                {(cart.Items && Object.keys(cart.Items).length !== 0) ? (
                    <>
                    <p>Your cart from</p>
                    <Link to={`/restaurants/${cart.restaurantId}`}>{cart.restaurant.name}</Link>
                    <div className="cart-price-details">
                        <div><p>{cart.totalItems} item{cart.totalItems > 1 ? "s" : ""}</p></div>
                        <div><p>Subtotal:${cart.totalCost}</p></div>
                    </div>
                    <ul className='cart-item-list'>
                        {Object.values(cart.Items).map(item => (
                            <li key={item.id}>
                                <CartItemTile itemData={item} orderId={cart.id}/>
                            </li>
                        ))}
                    </ul>
                    <div className='cart-checkout-div' onClick={() => history.push('/user/checkout')}>
                        <div>Checkout</div>
                        <div>${(Number(cart.totalCost) || 0).toFixed(2)}</div>
                    </div>
                    </>
                ) : (
                    <div className='empty-cart'>
                    <h2>Add items to start a cart</h2>
                    <p>Once you add items from a restaurant or store, your cart will appear here.</p>
                    <button id='continue-shopping-button' onClick={closeMenu}>Start shopping</button>
                    </div>
                )}
                </div> : (
                    <h1>Loading</h1>
                )}
            </div>
        </div>
    )
};

export default Cart;
