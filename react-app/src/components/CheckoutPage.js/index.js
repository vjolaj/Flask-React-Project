import React from "react";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./CheckoutPage.css"
import { checkOutCart, getCartThunk, newCartThunk } from "../../store/ordersReducer";
import OpenModalButton from "../OpenModalButton";
import CheckOutModal from "./checkoutModal";


export default function CheckoutPage() {
    let dispatch = useDispatch();
    let history = useHistory();
    const cart = useSelector((state) => {
        return state.orders.cart;
    })

    const [deliveryMethod, setDeliveryMethod] = useState("");
    const [paymentDetails, setPaymentDetails] = useState("");
    const [address, setAddress] = useState("");
    const [tip, setTip] = useState(0)
    const [fees, setFees] = useState(Number(((cart.totalCost) * 1.1) + 3.18) - cart.totalCost)
    const [totalPrice, setTotalPrice] = useState(0)

    const [deliveryTime, setDeliveryTime] = useState("")

    const [errors, setErrors] = useState({});

    useEffect(() => {
        dispatch(getCartThunk());
    }, [dispatch]);

    
    useEffect(() =>{ 
        setTotalPrice((Number(cart.totalCost) + fees + Number(tip)).toFixed(2))
    }, [tip])

    const handleSubmit = async () => {

        let errs = {}
        if (!deliveryMethod) errs.deliveryMethod = "Delivery method is required";
        else if (deliveryMethod.length > 50) errs.deliveryMethod = "Delivery method must be less than 50 characters";
        if (!paymentDetails) errs.paymentDetails = "Payment details are required";
        else if (paymentDetails.length > 50) errs.paymentDetails = "Payment Details must be less than 50 characters";
        if (!address) errs.address = "Address is required";
        else if (address.length > 50) errs.address = "Address must be less than 50 characters"
        if (!deliveryTime) errs.deliveryTime = "Please select a delivery estimate"

        if (Object.values(errs).length) {
            setErrors(errs)
        }
        else {
            const payload = {
                deliveryMethod,
                paymentDetails,
                address,
                isCompleted: true,
                totalPrice
            }
            let order;
            console.log("**********dispatching checkout*********", payload)
            order = await dispatch(checkOutCart(cart.id, payload))
            // const data = await order.json()
            // console.log("*********reutrn from dispatch checkout", data)

            if (order) {
                const newOrder = await dispatch(newCartThunk());
            }
        }

    }

    useEffect(() => {
        let errs = {}
        if (!deliveryMethod) errs.deliveryMethod = "Delivery method is required";
        else if (deliveryMethod.length > 50) errs.deliveryMethod = "Delivery method must be less than 50 characters";
        if (!paymentDetails) errs.paymentDetails = "Payment details are required";
        else if (paymentDetails.length > 50) errs.paymentDetails = "Payment Details must be less than 50 characters";
        if (!address) errs.address = "Address is required";
        else if (address.length > 50) errs.address = "Address must be less than 50 characters"
        if (!deliveryTime) errs.deliveryTime = "Please select a delivery estimate"

        setErrors(errs)
        console.log(errors)
    }, [deliveryMethod, paymentDetails, address, deliveryTime])

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
                            {errors.address && (
                                <p className="red">{errors.address}</p>
                            )}
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
                            {errors.deliveryMethod && (
                                <p className="red">{errors.deliveryMethod}</p>
                            )}
                        </div>
                    </div>
                </div>
                <div className="left-section">
                    <h3>Delivery estimate</h3>
                    {errors.deliveryTime && (
                        <p className="red">{errors.deliveryTime}</p>
                    )}
                    <div className="left-subsection">
                        <input type="radio" name="delivery-time" value="Priority" onClick={(e) => setDeliveryTime(e.target.value)}/>
                        <div className="space-between bottom-border">
                            <div>Priority</div>
                            <div>+$1.99</div>
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <input type="radio" name="delivery-time" value="Standard" onClick={(e) => setDeliveryTime(e.target.value)}/>
                        <div className="space-between">
                            <div>Standard</div>
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
                            {errors.paymentDetails && (
                                <p className="red">{errors.paymentDetails}</p>
                            )}
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
                    {/* <button
                        id="place-order-button"
                        onClick={handleSubmit}
                    >
                        Place Order
                    </button> */}
                    <div id="place-order-button">
                        <OpenModalButton
                                        id="place-order-button"
                                        buttonText="Place Order"
                                        onButtonClick={handleSubmit}
                                        onModalClose={() => history.push('/orders')}
                                        errors={Boolean(Object.values(errors).length)}
                                        modalComponent={
                                            <CheckOutModal/>
                                        }
                        ></OpenModalButton>
                    </div>
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
                        <h4>${(Number((cart.totalCost * 1.1) + 3.18) - cart.totalCost).toFixed(2)}</h4>
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
                            type='number'
                            min='0'
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
