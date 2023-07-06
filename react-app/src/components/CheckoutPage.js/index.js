import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import "./CheckoutPage.css"
import { editOrderThunk } from "../../store/ordersReducer";


export default function CheckoutPage() {


    return (
        <div id='checkout-wrapper'>
            <div id='checkout-left-side'>
                <div className="left-section">
                    <h2>Restaurant Name</h2>
                    <div className="left-subsection">
                        <i class="fa-solid fa-location-dot"></i>
                        <div className="space-between bottom-border">
                            <div>delivery address</div>
                            <input className="checkout-page-input"/>
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <i class="fa-solid fa-person"></i>
                        <div className="space-between">
                            <div>
                                <div>Meet at door</div>
                                <div>Add delivery instructions</div>
                            </div>
                            <input className="checkout-page-input"/>
                        </div>
                    </div>
                </div>
                <div className="left-section">
                    <h3>Delivery estimate</h3>
                    <div className="left-subsection">
                        <input type="checkbox"/>
                        <div className="space-between bottom-border">
                            <div>Priority</div>
                            <div>+$1.99</div>
                        </div>
                    </div>
                    <div className="left-subsection">
                        <input type="checkbox"/>
                        <div className="space-between bottom-border">
                            <div>Standard</div>
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <input type="checkbox"/>
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
                            <input className="checkout-page-input"/>
                        </div>
                    </div>
                    <div className="left-subsection bottom-border">
                        <i class="fa-solid fa-tag"></i>
                        <div className="space-between">
                            <div>Add promo code</div>
                            <input className="checkout-page-input"/>
                        </div>
                    </div>
                </div>
                <div className="left-section">
                    <div className="space-between">
                        <h3>Your items</h3>
                        <button className="checkout-page-button">
                            <i class="fa-solid fa-plus"></i> Add items
                        </button>
                    </div>
                    <div>insert items</div>
                </div>
            </div>
            <div id='checkout-right-side'>
                <div className="right-section bottom-border">
                    <button id='place-order-button'>Place order</button>
                    <p>If you’re not around when the delivery person arrives, they’ll leave your order at the door. By placing your order, you agree to take full responsibility for it once it’s delivered. Orders containing alcohol or other restricted items may not be eligible for leave at door and will be returned to the store if you are not available.</p>
                </div>
                <div className="right-section bottom-border">
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Subtotal</h4>
                            <i class="fa-solid fa-circle-info"></i>
                        </div>
                        <h4>order.totalCost</h4>
                    </div>
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Taxes & Other Fees</h4>
                            <i class="fa-solid fa-circle-info"></i>
                        </div>
                        <h4>order.totalCost + some other stuff</h4>
                    </div>
                </div>
                <div className="right-section bottom-border">
                    <div className="space-between">
                        <div className="info-button">
                            <h4>Add a tip</h4>
                            <i class="fa-solid fa-circle-info"></i>
                        </div>
                        <h4>tip amount</h4>
                    </div>
                    <p>100% of your tip goes to your courier. Tips are based on your order total of (insert total) before any discounts or promotions.</p>
                    <div id='tip-buttons'>
                        <button className="checkout-page-button">$2.00</button>
                        <button className="checkout-page-button">$3.00</button>
                        <button className="checkout-page-button">$4.00</button>
                        <button className="checkout-page-button">$5.00</button>
                        <input className="checkout-page-button"/>
                    </div>
                </div>
                <div className="right-section">
                    <div className="space-between">
                        <h3>Total</h3>
                        <h3>insert total</h3>
                    </div>
                </div>
            </div>
        </div>
      );
}
