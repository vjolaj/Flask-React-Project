import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { NavLink, Link } from "react-router-dom";
import { getUserRestaurantsThunk } from "../../store/restaurantsReducer";
import "./ManageRestaurants.css";
import OpenModalButton from "../OpenModalButton";
import DeleteRestaurantModal from "../DeleteRestaurantModal";
import NewMenuItemModal from "../NewMenuItemModal";

const ManageRestaurants = () => {
  const dispatch = useDispatch();
  const restaurants = useSelector((state) => state.restaurants.allRestaurants);
  console.log(restaurants);

  useEffect(() => {
    dispatch(getUserRestaurantsThunk());
  }, [dispatch]);

  if (!restaurants) return null;

  return (
    <div className="manage-rest-container">
      <div className="manageRestaurantsHeaders">
        <h2 className="manageHeader">Manage Spots</h2>
        <Link to="/restaurants/newrestaurant">
          <button className="addRestaurantButton">
            Create a New Restaurant
          </button>
        </Link>
      </div>
      <div className="rest-index-container">
        {Object.values(restaurants).map((restaurant) => (
          <div key={restaurant.id}>
            <div className="ManageSingleRestContainer">
              <div>
                <NavLink to={`/restaurants/${restaurant.id}`}>
                  <img
                    src={restaurant.imageUrl}
                    alt="img"
                    className="restImg"
                  />
                </NavLink>
              </div>
              <h3 className="name">{restaurant.name}</h3>
           
            <div className="manageSpot-buttons">
              {/* <Link to={`/spots/${spot.id}/edit`}>
            <button id="updateButton">Update</button>
          </Link> */}
          <div className="editButtons"></div>
              <div className="container">
          <div className="black-button">
                <OpenModalButton
                  buttonText="Add Menu Item"
                  modalComponent={<NewMenuItemModal restaurant={restaurant} />}
                />
              </div>
            <Link to={`/restaurants/${restaurant.id}/update`}>
              <button className="editRestaurant">
                Update Restaurant
              </button>
            </Link>
            </div>
            <div className="deleteRestaurantButton">
            <div className="black-button">
             <OpenModalButton
              buttonText="Delete Restaurant"
              modalComponent={
                <DeleteRestaurantModal restaurant={restaurant} />
              }
            />
            </div>
             </div>
            </div>
 </div>

          </div>
        ))}

      </div>
      
    </div>
  );
};

export default ManageRestaurants;
