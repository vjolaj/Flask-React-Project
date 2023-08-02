import React from "react";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./CheckoutPage.css"
import { checkOutCart, getCartThunk, newCartThunk } from "../../store/ordersReducer";
import CheckOutModal from "./checkoutModal";
import CheckoutItemTile from "./checkoutItemTile";


export default function CheckoutPage() {
    let dispatch = useDispatch();
    let history = useHistory();
    const cart = useSelector((state) => {
        return state.orders.cart;
    })

    const [deliveryMethod, setDeliveryMethod] = useState("");
    const [paymentDetails, setPaymentDetails] = useState("");
    const [address, setAddress] = useState("");
    const [tip, setTip] = useState("")
    const [customTip, setCustomTip] = useState(false)
    const [fees, setFees] = useState(Number(((cart.totalCost) * 1.1) + 3.18) - Number(cart.totalCost))
    const [deliveryTime, setDeliveryTime] = useState("")
    const [priorityPrice, setPriorityPrice] = useState(0)
    const [totalPrice, setTotalPrice] = useState(0)
    let [errors, setErrors] = useState({})

    useEffect(() => {
        dispatch(getCartThunk());
    }, [dispatch]);

    useEffect(() =>{
        setFees(Number(((cart.totalCost) * 1.1) + 3.18) - Number(cart.totalCost))
        if (deliveryTime === "Priority") setPriorityPrice(1.99)
        else if (deliveryTime === "Standard") setPriorityPrice(0)
        setTotalPrice((Number(cart.totalCost) + Number(priorityPrice) + Number(fees) + Number(tip)).toFixed(2))
    }, [tip, deliveryTime, cart, errors])

    const validate = () => {
        let errs = {}
        if (!deliveryMethod) errs.deliveryMethod = "Delivery method is required";
        else if (deliveryMethod.length > 50) errs.deliveryMethod = "Delivery method must be less than 50 characters";
        if (!paymentDetails) errs.paymentDetails = "Payment details are required";
        else if (paymentDetails.length > 50) errs.paymentDetails = "Payment Details must be less than 50 characters";
        if (!address) errs.address = "Address is required";
        else if (address.length > 50) errs.address = "Address must be less than 50 characters"
        if (!deliveryTime) errs.deliveryTime = "Please select a delivery estimate"

        errors = errs
        if (Object.keys(errs).length !== 0) {
            return {validated: false,
            errs}
        } else return {validated: true}
    }

    const handleSubmit = async () => {
        setErrors({})

        const {validated, errs} = validate()

        if (!validated) {
            setErrors({...errs})
            return errs
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
            order = await dispatch(checkOutCart(cart.id, payload))

            if (order) {
                const newOrder = await dispatch(newCartThunk());
            }
            history.push('/finalizing-checkout')
        }
    }

    const tipClassName = (value) => {
        if (customTip && value == 'Custom') {
            return "checkout-page-button-active"
        } else if (!customTip && Number(tip) === value) {
            return "checkout-page-button-active"
        } else {
            return "checkout-page-button"
        }
    }

    const paymentClassName = (value) => {
        if (paymentDetails == value) {
            return "checkout-page-button-active"
        } else {
            return "checkout-page-button"
        }
    }

    const deliveryClassName = (value) => {
        if (deliveryMethod == value) {
            return "checkout-page-button-active"
        } else {
            return "checkout-page-button"
        }
    }

    const helperSetTip = (value) => {
        setCustomTip(false)
        if (Number(tip) === Number(value)) setTip("")
        else if (Number(value) < 0) setTip("")
        else setTip(value)
    }
    const helperCustomTip = (value) => {
        setCustomTip(true)
        setTip(value)
    }

    const preventMinus = (e) => {
        if (e.code === 'Minus') {
            e.preventDefault();
        }
    };

    const twoDecimal = (e) => {
        if (!/^\d*(\.\d{0,2})?$/.test(e.target.value)) {
            e.target.value = Number(e.target.value).toFixed(2)
        }
        setTip(e.target.value)
    }


    if (!cart.restaurant) return null

    return (
        <div id='checkout-wrapper'>
            <div id='checkout-left-side'>
                <div className="left-section">
                    <div id='checkout-restaurant' onClick={() => history.push(`/restaurants/${cart.restaurantId}`)}>
                        <img src={cart.restaurant.imageUrl}/>
                        <h2>{cart.restaurant.name}</h2>
                    </div>
                    <div className="left-subsection">
                        <i className="fa-solid fa-location-dot"></i>
                        <div className="space-between bottom-border">
                            <div>Address: </div>
                            {errors.address && (
                                <p className="red">{errors.address}</p>
                            )}
                            <input
                                className="checkout-page-input"
                                placeholder="Enter Your Address"
                                onChange={(e) => {
                                    setAddress(e.target.value)
                                }}
                                defaultValue={address}
                            />
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <i className="fa-solid fa-person"></i>
                        <div className="space-between">
                            <div>
                                <div>Delivery Method: </div>
                            </div>
                            {errors.deliveryMethod && (<p className="red">{errors.deliveryMethod}</p>)}
                            <div id='delivery-choice'>
                                <button
                                    className={deliveryClassName('Pickup')}
                                    onClick={() => setDeliveryMethod("Pickup")}
                                    value="Pickup"
                                >
                                    Pickup
                                </button>
                                <button
                                    className={deliveryClassName('Delivery')}
                                    onClick={() => setDeliveryMethod("Delivery")}
                                    value="Delivery"
                                >
                                    Delivery
                                </button>
                            </div>

                            {/* <fieldset name='delivery-method' className="fieldset-delivery">
                                <div className="left-subsection delivery-choices">
                                    <input type="radio" name="delivery-method" className='radio-delivery' value="Pickup" onChange={(e) =>
                                    setDeliveryMethod(e.target.value)}/>
                                    <div className="space-between">
                                        <label htmlFor='delivery-method'>Pickup</label>
                                    </div>
                                </div>
                                <div className="left-subsection">
                                    <input type="radio" name="delivery-method" value="Delivery" onChange={(e) => setDeliveryMethod(e.target.value)
                                    } />
                                    <div className="space-between">
                                        <label htmlFor='delivery-method'>Delivery</label>
                                    </div>
                                </div>
                            </fieldset> */}
                        </div>
                    </div>
                </div>
                <div className="left-section">
                    <h3>Delivery estimate</h3>
                    {errors.deliveryTime && (
                        <p className="red">{errors.deliveryTime}</p>
                    )}
                    <fieldset name='delivery-estimate' className="fieldset-priority">
                        <div className="left-subsection bottom-border">
                            <input type="radio" name="delivery-time" value="Priority" onChange={(e) =>
                                setDeliveryTime(e.target.value)}/>
                            <div className="space-between">
                                <label htmlFor='delivery-time'>Standard</label>
                            </div>
                        </div>
                        <div className="left-subsection bottom-border">
                            <input type="radio" name="delivery-time" value="Standard" onChange={(e) =>
                                setDeliveryTime(e.target.value)} />
                            <div className="space-between">
                                <label htmlFor='delivery-time'>Priority</label>
                                <div>+$1.99</div>
                            </div>
                        </div>
                    </fieldset>
                </div>
                <div className="left-section">
                    <h3>Payment</h3>
                    <div className="left-subsection">
                        <i className="fa-regular fa-credit-card"></i>
                        <div className="space-between bottom-border">
                            <label>Payment Type: </label>
                            {errors.paymentDetails && (<p className="red">{errors.paymentDetails}</p>)}
                            <div id='payment-choice'>
                                <button
                                    className={paymentClassName('PayPal')}
                                    onClick={() => setPaymentDetails("PayPal")}
                                    value="PayPal"
                                >
                                    <i class="fa-brands fa-paypal"></i>
                                </button>
                                <button
                                    className={paymentClassName('Visa')}
                                    onClick={() => setPaymentDetails("Visa")}
                                    value="Visa"
                                >
                                    <i class="fa-brands fa-cc-visa"></i>
                                </button>
                                <button
                                    className={paymentClassName('MasterCard')}
                                    onClick={() => setPaymentDetails("MasterCard")}
                                    value="MasterCard"
                                >
                                    <i class="fa-brands fa-cc-mastercard"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <i className="fa-solid fa-tag"></i>
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
                        <button className="checkout-page-button" onClick={() => history.push(`/restaurants/${cart.restaurantId}`)}>
                            <i className="fa-solid fa-plus"></i> Add items
                        </button>
                    </div>
                    <div>
                        {Object.values(cart.Items).map(item => (
                            <div key={item.id}>
                                <CheckoutItemTile itemData={item} />
                            </div>
                        ))}
                    </div>
                </div>
            </div>
            <div id='checkout-right-side'>
                <div className="right-section bottom-border">
                    <div id="place-order-button">
                        <button onClick={handleSubmit}>Place Order</button>
                    </div>
                    <p>If you’re not around when the delivery person arrives, they’ll leave your order at the door. By placing your order, you agree to take full responsibility for it once it’s delivered. Orders containing alcohol or other restricted items may not be eligible for leave at door and will be returned to the store if you are not available.</p>
                </div>
                <div className="right-section bottom-border">
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Subtotal</h4>
                            {/* <i className="fa-solid fa-circle-info"></i> */}
                        </div>
                        <h4>${Number(cart.totalCost).toFixed(2)}</h4>
                    </div>
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Taxes & Other Fees</h4>
                            {/* <i name="fa-solid fa-circle-info"></i> */}
                        </div>
                        <h4>${(Number((cart.totalCost * 1.1) + 3.18) - cart.totalCost).toFixed(2)}</h4>
                    </div>
                </div>
                <div className="right-section bottom-border">
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Add a tip</h4>
                            {/* <i className="fa-solid fa-circle-info"></i> */}
                        </div>
                        <h4>${Number(tip).toFixed(2)}</h4>
                    </div>
                    <p>100% of your tip goes to your courier. Tips are based on your order total of ${Number((cart.totalCost * 1.1) + 3.18).toFixed(2)} before any discounts or promotions.</p>
                    <div id='tip-buttons'>
                        <button
                            className={tipClassName(2.00)}
                            value={2.00}
                            onClick={(e) => helperSetTip(e.target.value)}
                        >$2.00</button>
                        <button
                            className={tipClassName(3.00)}
                            value={3.00}
                            onClick={(e) => helperSetTip(e.target.value)}
                        >$3.00</button>
                        <button
                            className={tipClassName(4.00)}
                            value={4.00}
                            onClick={(e) => helperSetTip(e.target.value)}
                        >$4.00</button>
                        <button
                            className={tipClassName(5.00)}
                            value={5.00}
                            onClick={(e) => helperSetTip(e.target.value)}
                        >$5.00</button>
                        <div id='custom-tip-wrap'>
                            <div id='dollar-sign' className={customTip? 'white' : 'black'}>$</div>
                            <input
                                id='custom-tip'
                                className={tipClassName('Custom')}
                                onChange={twoDecimal}
                                onClick={(e) => helperCustomTip(e.target.value)}
                                type="number" min="0"
                                step='0.01'
                                pattern="^\d*(\.\d{0,2})?$"
                                onKeyPress={preventMinus}
                            />
                        </div>
                    </div>
                </div>
                <div className="right-section">
                    <div className="space-between">
                        <h3>Total</h3>
                        <h3>${totalPrice}</h3>
                    </div>
                </div>
            </div>
        </div>
      );
}
