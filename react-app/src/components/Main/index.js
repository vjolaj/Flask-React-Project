import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { removeFilter, receiveFilter } from "../../store/filterReducer";
import RestaurantsIndex from "../RestaurantsIndex";
import "./main.css";
import { newCartThunk, getCartThunk } from "../../store/ordersReducer";
import { NavLink, useHistory } from "react-router-dom";

const CATEGORIES = {
  Pizza: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/pizza.png",
  Mexican: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/mexican.png",
  FastFood: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/fastfood.png",
  Sandwich: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/sandwich.png",
  Asian: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/asian.png",
  American: "https://oobreats.s3.amazonaws.com/american.png",
  Chinese: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/chinese.png",
  Italian: "https://oobreats.s3.amazonaws.com/italian.png",
  Sushi: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/sushi.png",
  Healthy: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/healthy.png",
};

const Main = () => {
  const dispatch = useDispatch();
  const restaurants = useSelector((state) => state.restaurants.allRestaurants);
  const filter = useSelector((state) => state.filter.type);
  const cart = useSelector((state) => state.orders.cart);
  const history = useHistory();

  useEffect(() => {
    dispatch(getCartThunk());
    if (!cart) {
      dispatch(newCartThunk());
    }
  }, [dispatch]);

  const handleFilterClick = (cuisineType) => {
    if (filter === cuisineType) {
      dispatch(removeFilter());
    } else {
      dispatch(receiveFilter(cuisineType));
    }
  };

  const filteredRestaurants = filter
    ? Object.values(restaurants).filter((restaurant) => restaurant.cuisineType === filter)
    : Object.values(restaurants);

  const showNoRestaurantsMessage = filter && filteredRestaurants.length === 0;

  return (
    <div>
      <div className="categories-container">
        {Object.keys(CATEGORIES).map((cuisineType, i) => (
          <button
            onClick={() => handleFilterClick(cuisineType)}
            key={i}
            className={`singleCategory ${filter === cuisineType ? "active" : ""}`}
          >
            <img src={CATEGORIES[cuisineType]} alt={cuisineType} className="singleCategory" />
            <div className="categories-name">{cuisineType}</div>
          </button>
        ))}
      </div>

      {showNoRestaurantsMessage ? (
        <div className="apologize">
          <p className="apologize">
            We apologize, but there are currently no restaurants available for this category.
          </p>
          <img
            src="https://www.cambridge.org/elt/blog/wp-content/uploads/2019/07/Sad-Face-Emoji.png"
            alt="sad-face"
            className="sadFace"
          />
        </div>
      ) : (
        <div>
          <RestaurantsIndex restaurants={filteredRestaurants} />
        </div>
      )}
    </div>
  );
};

export default Main;

