import React, { useState } from "react";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllRestaurantsThunk } from "../../store/restaurantsReducer";
import "./restaurantIndex.css";
import { removeFilter } from "../../store/filterReducer";

const RestaurantsIndex = ({ restaurants }) => {
  const dispatch = useDispatch();
  const [selectedPriceRange, setSelectedPriceRange] = useState(null);

  useEffect(() => {
    dispatch(getAllRestaurantsThunk());
  }, [dispatch]);

  if (!restaurants) return null;

  const getRandomDeliveryFee = () => {
    const fees = ["$3.99", "$5.99", "$2.49", "$1.49", "$0.99", "Free"];
    return fees[Math.floor(Math.random() * fees.length)];
  };

  const handlePriceRangeChange = (priceRange) => {
    if (selectedPriceRange === priceRange) {
      setSelectedPriceRange(null);
      dispatch(removeFilter());
    } else {
      setSelectedPriceRange(priceRange);
    }
  };

  const handleAll = () => {
    setSelectedPriceRange(null);
    dispatch(removeFilter());
  };

  const filteredRestaurants = selectedPriceRange
    ? restaurants.filter((restaurant) => restaurant.priceRange === selectedPriceRange)
    : restaurants;

  return (
    <div className="main-filter-items">
      <div className="item-type-filter-main">
        <div className="all-main">
          <h2>All Restaurants</h2>
          <p className="sort">Sort</p>
          <button onClick={handleAll} className={selectedPriceRange === null}>
            <p className="clear">Clear all</p>
          </button>
        </div>
        <p className="price">Price Range</p>
        <div className="dollar-buttoms">
          <button
            onClick={() => handlePriceRangeChange("$")}
            className={selectedPriceRange === "$" ? "active" : ""}
          >
            $
          </button>
          <button
            onClick={() => handlePriceRangeChange("$$")}
            className={selectedPriceRange === "$$" ? "active" : ""}
          >
            $$
          </button>
          <button
            onClick={() => handlePriceRangeChange("$$$")}
            className={selectedPriceRange === "$$$" ? "active" : ""}
          >
            $$$
          </button>
          <button
            onClick={() => handlePriceRangeChange("$$$$")}
            className={selectedPriceRange === "$$$$" ? "active" : ""}
          >
            $$$$
          </button>
        </div>
      </div>
      <div className="rest-index-container">
        {filteredRestaurants.map((restaurant) => (
          <div key={restaurant.id} onClick={handleAll}>
            <div className="singleRestContainer">
              <div>
                <NavLink to={`/restaurants/${restaurant.id}`}>
                  <img src={restaurant.imageUrl} alt="img" className="restImg" />
                </NavLink>
              </div>
              <p className="main-name">{restaurant.name}</p>
              <p className="delivery-fee-main">{getRandomDeliveryFee()} Delivery Fee</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RestaurantsIndex;

