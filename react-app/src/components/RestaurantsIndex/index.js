import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import { getAllRestaurantsThunk } from "../../store/restaurantsReducer";
import "./restaurantIndex.css";

const RestaurantsIndex = ({ restaurants }) => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllRestaurantsThunk());
  }, [dispatch]);

  if (!restaurants) return null;

  return (
    <div className="rest-index-container">
      {restaurants.map((restaurant) => (
        <div key={restaurant.id}>
          <div className="singleRestContainer">
            <div>
              <NavLink to={`/restaurants/${restaurant.id}`}>
                <img src={restaurant.imageUrl} alt="img" className="restImg" />
              </NavLink>
            </div>
            <h2>{restaurant.name}</h2>
          </div>
        </div>
      ))}
    </div>
  );
};

export default RestaurantsIndex;
