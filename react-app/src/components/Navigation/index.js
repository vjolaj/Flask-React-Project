import React, { useState, useEffect, useRef } from "react";
import { NavLink, useLocation, Route, Switch } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import { removeFilter } from "../../store/filterReducer";
// import OpenModalButton from "../OpenModalButton";
import { useDispatch } from "react-redux";
// import { useHistory } from "react-router-dom";
import Cart from "../Cart";

import "./Navigation.css";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const cart = useSelector((state) => state.session.cart);
  const dispatch = useDispatch();
  const location = useLocation();

  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleEpicEatsClick = () => {
    dispatch(removeFilter()); // Dispatch the removeFilter action
  };

  const openCart = () => {
    return;
  };

  const showSearchBar = location.pathname === "/restaurants";

  return (
    <div className="nav">
      <div className="navLeft">
        <div className="userButton">
          <ProfileButton user={sessionUser} className="userButton" />
        </div>
        <div className="logo">
          <p>
            <NavLink
              exact
              to="/restaurants"
              className="logo"
              onClick={handleEpicEatsClick}
            >
              Epic
            </NavLink>
          </p>
          <p>
            <NavLink exact to="/restaurants" className={location.pathname === "/" ? "Eats-black" : "Eats"} onClick={handleEpicEatsClick}>Eats</NavLink>
          </p>
        </div>
      </div>
      {showSearchBar && (
        <div className="search-bar">
          <i class="fa-sharp fa-solid fa-magnifying-glass"></i>
          <input type="text" placeholder="Search feature coming soon" />
        </div>
      )}
      <Switch>
        <Route path="/restaurants">
          <div className="cart" onClick={openCart}>
            <Cart />
          </div>
        </Route>
      </Switch>
    </div>
  );
}

export default Navigation;
