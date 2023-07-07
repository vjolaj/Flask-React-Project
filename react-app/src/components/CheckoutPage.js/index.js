import React from "react";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./CheckoutPage.css"
import { checkOutCart, getCartThunk, newCartThunk } from "../../store/ordersReducer";


export default function CheckoutPage() {
    let dispatch = useDispatch();
    let history = useHistory();
    const cart = useSelector((state) => {
        return state.orders.cart;
    })

    const [deliveryMethod, setDeliveryMethod] = useState(cart ? cart.deliveryMethod : "");
    const [paymentDetails, setPaymentDetails] = useState(cart ? cart.paymentDetails : "");
    const [address, setAddress] = useState(cart ? cart.address : "");

    const [tip, setTip] = useState(0)

    const [errors, setErrors] = useState({});

    useEffect(() => {
        dispatch(getCartThunk());
    }, [dispatch]);


    const handleSubmit = async (e) => {
        e.preventDefault();

        let errs = {}
        if (!deliveryMethod) errs.deliveryMethod = "Delivery method is required";
        if (!paymentDetails) errs.paymentDetails = "Payment details are required";
        if (!address) errs.address = "Address is required";

        const payload = {
            deliveryMethod,
            paymentDetails,
            address
        }
        let order;
        order = await dispatch(checkOutCart(cart.id, payload))

        if (order) {
            order = await dispatch(newCartThunk());
        }
    }

    return (
        <div id='checkout-wrapper'>
            <div id='checkout-left-side'>
                <div className="left-section">
                    <h2>Restaurant Name</h2>
                    <div className="left-subsection">
                        <i class="fa-solid fa-location-dot"></i>
                        <div className="space-between bottom-border">
                            <div>Address: {address}</div>
                            <input
                                className="checkout-page-input"
                                placeholder="Enter Your Address"
                                onChange={(e) => setAddress(e.target.value)}
                                defaultValue={address}
                            />
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <i class="fa-solid fa-person"></i>
                        <div className="space-between">
                            <div>
                                <div>Delivery Method: {deliveryMethod}</div>
                            </div>
                            <input
                                className="checkout-page-input"
                                placeholder="e.g. Pickup/Delivery"
                                onChange={(e) => setDeliveryMethod(e.target.value)}
                                defaultValue={deliveryMethod}
                            />
                        </div>
                    </div>
                </div>
                <div className="left-section">
                    <h3>Delivery estimate</h3>
                    <div className="left-subsection">
                        <input type="radio" name="delivery-time"/>
                        <div className="space-between bottom-border">
                            <div>Priority</div>
                            <div>+$1.99</div>
                        </div>
                    </div>
                    <div className="left-subsection">
                        <input type="radio" name="delivery-time"/>
                        <div className="space-between bottom-border">
                            <div>Standard</div>
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <input type="radio" name="delivery-time"/>
                        <div>
                            <div>Schedule</div>
                        </div>
                    </div>
                </div>
                <div className="left-section">
                    <h3>Payment</h3>
                    <div className="left-subsection">
                        <i class="fa-regular fa-credit-card"></i>
                        <div className="space-between bottom-border">
                            <div>Credit or Debit Card</div>
                            <input
                                className="checkout-page-input"
                                placeholder="Enter payment info"
                                onChange={(e) => setPaymentDetails(e.target.value)}
                                defaultValue={paymentDetails}
                            />
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <i class="fa-solid fa-tag"></i>
                        <div className="space-between">
                            <div>Add promo code</div>
                            <input
                                className="checkout-page-input"
                                placeholder="Enter promo code"
                            />
                        </div>
                    </div>
                </div>
                <div className="left-section">
                    <div className="space-between">
                        <h3>Your items</h3>
                        <button className="checkout-page-button" onClick={() => history.push('/restaurants')}>
                            <i class="fa-solid fa-plus"></i> Add items
                        </button>
                    </div>
                    <div>insert items</div>
                </div>
            </div>
            <div id='checkout-right-side'>
                <div className="right-section bottom-border">
                    <button id='place-order-button' onClick={handleSubmit}>Place order</button>
                    <p>If you’re not around when the delivery person arrives, they’ll leave your order at the door. By placing your order, you agree to take full responsibility for it once it’s delivered. Orders containing alcohol or other restricted items may not be eligible for leave at door and will be returned to the store if you are not available.</p>
                </div>
                <div className="right-section bottom-border">
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Subtotal</h4>
                            <i class="fa-solid fa-circle-info"></i>
                        </div>
                        <h4>${Number(cart.totalCost).toFixed(2)}</h4>
                    </div>
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Taxes & Other Fees</h4>
                            <i class="fa-solid fa-circle-info"></i>
                        </div>
                        <h4>${Number((cart.totalCost * 1.1) + 3.18).toFixed(2)}</h4>
                    </div>
                </div>
                <div className="right-section bottom-border">
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Add a tip</h4>
                            <i class="fa-solid fa-circle-info"></i>
                        </div>
                        <h4>${Number(tip).toFixed(2)}</h4>
                    </div>
                    <p>100% of your tip goes to your courier. Tips are based on your order total of (insert total) before any discounts or promotions.</p>
                    <div id='tip-buttons'>
                        <button
                            className="checkout-page-button"
                            value={2.00}
                            onClick={(e) => setTip(e.target.value)}
                        >$2.00</button>
                        <button
                            className="checkout-page-button"
                            value={3.00}
                            onClick={(e) => setTip(e.target.value)}
                        >$3.00</button>
                        <button
                            className="checkout-page-button"
                            value={4.00}
                            onClick={(e) => setTip(e.target.value)}
                        >$4.00</button>
                        <button
                            className="checkout-page-button"
                            value={5.00}
                            onClick={(e) => setTip(e.target.value)}
                        >$5.00</button>
                        <input
                            className="checkout-page-button"
                            placeholder="Other"
                            onChange={(e) => setTip(e.target.value)}
                        />
                    </div>
                </div>
                <div className="right-section">
                    <div className="space-between">
                        <h3>Total</h3>
                        <h3>${((cart.totalCost * 1.1) + 3.18 + Number(tip)).toFixed(2)}</h3>
                    </div>
                </div>
            </div>
        </div>
      );
}
