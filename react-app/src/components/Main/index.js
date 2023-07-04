import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { removeFilter, receiveFilter } from "../../store/filter_reducer";
import RestaurantsIndex from "../RestaurantsIndex";

const CATEGORIES = {
  Pizza: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/pizza.png", 
  Mexican: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/mexican.png",
  Sandwich:"https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/sandwich.png",
  Asian: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/asian.png",
  Chinese: "https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/chinese.png",
  Italian: "https://oobreats.s3.amazonaws.com/italian.png",
  Sushi: 'https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/sushi.png',
  Healthy: 'https://d4p17acsd5wyj.cloudfront.net/shortcuts/cuisines/healthy.png',
};

const Main = () => {
  const dispatch = useDispatch();
  const restaurants = useSelector((state) => state.restaurants.allRestaurants);
  const filter = useSelector((state) => state.filter.type);

  const handleFilterClick = (cuisineType) => {
      dispatch(receiveFilter(cuisineType));
  };

  const filteredRestaurants = filter
    ? Object.values(restaurants).filter(
        (restaurant) => restaurant.cuisineType === filter
      )
    : Object.values(restaurants);

    const showNoRestaurantsMessage =
    filter && filteredRestaurants.length === 0;

  return (
    <div>
      <div>
        {Object.keys(CATEGORIES).map((cuisineType, i) => (
          <button onClick={() => handleFilterClick(cuisineType)} key={i}>
            <img src={CATEGORIES[cuisineType]} alt={cuisineType} />
            <div>{cuisineType}</div>
          </button>
        ))}
      </div>

       {showNoRestaurantsMessage ? (
        <p>Sorry, there are no restaurants available for this category yet.</p>
      ) : (
        <RestaurantsIndex restaurants={filteredRestaurants} />
      )}
    </div>
  );
};

export default Main;