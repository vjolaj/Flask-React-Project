import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Link } from "react-router-dom";
import { getUserRestaurantsThunk } from "../../store/restaurantsReducer";
import "./ManageRestaurants.css";
import OpenModalButton from "../OpenModalButton";
import DeleteRestaurantModal from "../DeleteRestaurantModal";

const ManageRestaurants = () => {
  const dispatch = useDispatch();
  const restaurants = useSelector((state) => state.restaurants.allRestaurants);
  console.log(restaurants);

  useEffect(() => {
    dispatch(getUserRestaurantsThunk());
  }, [dispatch]);

  if (!restaurants) return null;

  return (
    <>
      {/* {!restaurants ? (
        <div className="manageRestaurantsHeaders">
          <div className="manageHeader">Manage Spots</div>
          <Link to="/restaurants/newrestaurant">
            <button className="addRestaurantButton">Create a New Restaurant</button>
          </Link>
        </div>
      ) : ( */}
      <div className="manageRestaurantsHeaders">
        <div className="manageHeader">Manage Spots</div>
        <Link to="/restaurants/newrestaurant">
          <button className="addRestaurantButton">
            Create a New Restaurant
          </button>
        </Link>
      </div>
      <div className="rest-index-container">
        {Object.values(restaurants).map((restaurant) => (
          <div key={restaurant.id}>
            <div className="singleRestContainer">
              <div>
                <NavLink to={`/restaurants/${restaurant.id}`}>
                  <img
                    src={restaurant.imageUrl}
                    alt="img"
                    className="restImg"
                  />
                </NavLink>
              </div>
              <h2>{restaurant.name}</h2>
            </div>
            <div className="manageSpot-buttons">
              {/* <Link to={`/spots/${spot.id}/edit`}>
            <button id="updateButton">Update</button>
          </Link> */}
              <OpenModalButton
                buttonText="Delete Restaurant"
                modalComponent={<DeleteRestaurantModal restaurant={restaurant} />}
              />
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default ManageRestaurants;