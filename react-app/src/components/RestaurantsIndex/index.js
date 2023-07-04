import React from 'react';
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { getAllRestaurantsThunk } from '../../store/restaurantsReducer';


const RestaurantsIndex = () => {
  const dispatch = useDispatch();
  let restaurants = useSelector((state) => state.restaurants.allRestaurants);
  console.log(restaurants,'⭐️')
//   restaurants = Object.values(restaurants)

  useEffect(() => {
    dispatch(getAllRestaurantsThunk());
  }, [dispatch]);

 if(!restaurants) return null

  return (
   <div>
      
      {Object.values(restaurants).map((restaurant) => (
        <div key={restaurant.id}>
          <h2>{restaurant.name}</h2>
        </div>
      ))}
    </div>

  
  );
};

export default RestaurantsIndex