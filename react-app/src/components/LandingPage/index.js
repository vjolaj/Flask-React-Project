import { NavLink } from "react-router-dom";
import { useSelector } from "react-redux";
import React from "react";
import "./landing.css";
import { useEffect } from "react";

// import { useDispatch, useSelector } from 'react-redux';

const LandingPage = () => {
  return (
    <>
      <div className="landingBack">
        <div className="landing-nav-right">
          <button>
            <NavLink exact to="/login"></NavLink> Login
          </button>
          <button>
            <NavLink exact to="/signup"></NavLink> Sign Up
          </button>
        </div>

        <h1 className="orderFood">Order food to your Door</h1>
        <img
          className="main-bg"
          src="https://oobreats.s3.amazonaws.com/splash6.webp"
          alt=""
        />
      </div>
    </>
  );
};

export default LandingPage;
