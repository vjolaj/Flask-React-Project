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
  const sessionUser = useSelector(state => state.session.user);
  const rest = useSelector((state) => state.restaurants.allRestaurants);

  useEffect(() => {
    dispatch(getUserRestaurantsThunk());
  }, [dispatch]);

  const restaurants = Object.values(rest).filter(
    (rest) => rest.ownerId === sessionUser.id
  );

  if (!restaurants) return null;

  return (
    <div className="manage-rest-container">
      <div className="manageRestaurantsHeaders">
        <div className="manageHeader">Manage Restaurants</div>
        <Link to="/restaurants/newrestaurant">
          <button className="addRestaurantButton">
            Create a New Restaurant
          </button>
        </Link>
      </div>
      <div className="manage-rest-index-container">
        {Object.values(restaurants).map((restaurant) => (
          <div key={restaurant.id}>
            <div>
              <NavLink to={`/restaurants/${restaurant.id}`}>
                <div className="manageRestImg">
                  <img
                    src={restaurant.imageUrl}
                    alt="img"
                    className="imageOverlay"
                  />
                  <div className="textOverlay">
                    <div className="restaurantName">{restaurant.name}</div>
                    <div className="restaurantAddress">
                      {restaurant.address}
                    </div>
                    <div className="manageSpot-buttons">
                      <div>
                        <OpenModalButton
                          buttonText="Add Menu Item"
                          modalComponent={
                            <NewMenuItemModal restaurant={restaurant} />
                          }
                        />
                      </div>
                      <Link to={`/restaurants/${restaurant.id}/update`}>
                        <button className="editRestaurant">
                          Update Restaurant
                        </button>
                      </Link>
                      <div className="deleteRestaurantButton">
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
              </NavLink>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ManageRestaurants;