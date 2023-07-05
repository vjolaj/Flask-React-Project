import React, { useEffect, useState, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';

const Cart = ({ user }) => {
    const dispatch = useDispatch();
    const history = useHistory();
    const modalRef = useRef();

    const cart = useSelector(state => state.session.cart)
    const [showMenu, setShowMenu] = useState(false);
    const [restaurantName, setRestaurantName] = useState("")

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
    }, [showMenu]);    

    const closeMenu = () => setShowMenu(false);

    const cartClassName = "cart-dropdown" + (showMenu ? "" : " hidden");

    return (
        <div className='cart-modal'>
            <button onClick={openMenu} className='cart-button'>
                <i class="fa-solid fa-cart-shopping"></i>
            </button>
            <div className={cartClassName} ref={modalRef}>
                {user ? (
                    <div>
                <div>
                    <i class="fa-solid fa-x"></i>
                </div>
                        <h3>Add items to start a cart</h3>
                        <p>Once you add items from a restaurant or store, your cart will appear here.</p>
                        <button onClick={closeMenu}>Start Shopping</button>
                    </div>
                ) : (
                    <div>
                        {/* <h2>{restaurantName}</h2> */}
                    </div>
                )}
            </div>
        </div>
    )
};

export default Cart;