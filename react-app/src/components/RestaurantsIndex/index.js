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

   const getRandomDeliveryFee = () => {
    const fees = ["$3.99", "$5.99", "$2.49", "$1.49", "$0.99", 'Free'];
    return fees[Math.floor(Math.random() * fees.length)];
  };

  
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
            <p className="main-name">{restaurant.name}</p>
            <p className="delivery-fee-main">{getRandomDeliveryFee()} Delivery Fee</p>
            
          </div>
        </div>
      ))}
    </div>
  );
};

export default RestaurantsIndex;
