import React, { useState, useEffect, useRef } from "react";
import { NavLink, useLocation, Route, Switch } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import { removeFilter } from "../../store/filterReducer";
// import OpenModalButton from "../OpenModalButton";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import Cart from "../Cart";
import { getAllRestaurantsThunk } from "../../store/restaurantsReducer";
import "./Navigation.css";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const cart = useSelector((state) => state.session.cart);
  const dispatch = useDispatch();
  const location = useLocation();
  const history = useHistory();
  const restaurants = useSelector((state) => state.restaurants.allRestaurants);
  const [search, setSearch] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  // const [showMenu, setShowMenu] = useState(false);
  const [showResultsContainer, setShowResultsContainer] = useState(false);
  const ulRef = useRef();

  useEffect(() => {
    dispatch(getAllRestaurantsThunk());
  }, [dispatch]);

  // useEffect(() => {
  //   if (!showMenu) return;

  //   const closeMenu = (e) => {
  //     if (!ulRef.current.contains(e.target)) {
  //       setShowMenu(false);
  //     }
  //   };

  //   document.addEventListener("click", closeMenu);

  //   return () => document.removeEventListener("click", closeMenu);
  // }, [showMenu]);

  const handleEpicEatsClick = () => {
    dispatch(removeFilter()); // Dispatch the removeFilter action
  };

  const openCart = () => {
    return;
  };

  const showSearchBar = location.pathname === "/restaurants";

  const handleSearchChange = (e) => {
    setSearch(e.target.value.toLowerCase());

    if (e.target.value.trim() === "") {
      setSearchResults([]);
      setSubmitted(false);
    }
  };

  const handleSearchSubmit = () => {
    setSubmitted(true);
    const filteredRestaurants = Object.values(restaurants).filter(
      (restaurant) =>
        restaurant.name.toLowerCase().includes(search) ||
        restaurant.menuItems.some((item) => item.toLowerCase().includes(search))
    );

    setSearchResults(filteredRestaurants);
  };

  const handleSearchKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSearchSubmit();
    }
  };

  const showSearchResults = location.pathname === "/restaurants"; // Check if the location is "/restaurants"

  useEffect(() => {
    return () => {
      setSearch("");
      setSearchResults([]);
      setSubmitted(false);
    };
  }, [location.pathname]);

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
            <NavLink
              exact
              to="/restaurants"
              className={location.pathname === "/" ? "Eats-black" : "Eats"}
              onClick={handleEpicEatsClick}
            >
              Eats
            </NavLink>
          </p>
        </div>
      </div>
      <div className="search-container">
        {showSearchBar && (
          <div className="search-bar">
            <i class="fa-sharp fa-solid fa-magnifying-glass"></i>
            <input
              type="text"
              placeholder="Search by restaurant name or menu item"
              value={search}
              onChange={handleSearchChange}
              onKeyDown={handleSearchKeyDown}
              onFocus={() => setShowResultsContainer(true)}
            />
          </div>
        )}
        <div
          className={`${
            submitted && searchResults
              ? "results-container-white-bg"
              : "results-container"
          }`}
        >
          {searchResults.length > 0 &&
            searchResults.map((restaurant) => (
              <div
                className="search-restaurant-div"
                onClick={() => history.push(`/restaurants/${restaurant.id}`)}
                key={restaurant.id}
              >
                {restaurant.name}
              </div>
            ))}
          {submitted && searchResults.length === 0 && search.length > 0 && (
            <div>No restaurants found, please try again</div>
          )}
        </div>
      </div>
      <div className="right-side-buttons">
        <Switch>
          <Route path="/restaurants">
            <button
              className="cart-button orders-nav-button"
              onClick={() => history.push("/orders")}
            >
              Past Orders
            </button>
            <div className="cart" onClick={openCart}>
              <Cart />
            </div>
          </Route>
        </Switch>
      </div>
    </div>
  );
}

export default Navigation;
