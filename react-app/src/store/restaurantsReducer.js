//constants
const GET_ALL_RESTAURANTS = "/restaurants/GET/all";
const GET_SINGLE_RESTAURANT = "/restaurant/GET/single";
const DELETE_SINGLE_RESTAURANT = "/restaurant/DELETE/single";

//action creators
const readAllRestaurantsAction = (restaurants) => {
  return {
    type: GET_ALL_RESTAURANTS,
    restaurants,
  };
};

const readSingleRestaurantAction = (restaurant) => {
  return {
    type: GET_SINGLE_RESTAURANT,
    restaurant,
  };
};

const deleteRestaurantAction = (restaurant) => {
  return {
    type: DELETE_SINGLE_RESTAURANT,
    restaurant,
  };
};

//thunks
export const getAllRestaurantsThunk = () => async (dispatch) => {
  const res = await fetch("/api/restaurants");

  const data = await res.json();

  const normalizedData = {};
  Object.values(data.all_restaurants).forEach((restaurant) => {
    normalizedData[restaurant.id] = restaurant;
  });

  dispatch(readAllRestaurantsAction(normalizedData));
  return data;
};

export const readSingleRestaurantThunk = (restaurant) => async (dispatch) => {
  dispatch(readSingleRestaurantAction(restaurant));

  return restaurant;
};

export const createRestaurantThunk = (restaurant) => async (dispatch) => {
  const {
    name,
    address,
    cuisine_type,
    price_range,
    imageUrl,
    rating,
    description,
  } = restaurant;

  const res = await fetch("/api/restaurants", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name,
      address,
      cuisine_type,
      price_range,
      imageUrl,
      rating,
      description,
    }),
  });

  const data = await res.json();

  //we can add menu items here or we can do this in another thunk if we end up using 2 pages for adding restaurant details and then menu

  return data;
};

export const editRestaurantThunk = (restaurant) => async (dispatch) => {
  const {
    name,
    address,
    cuisine_type,
    price_range,
    imageUrl,
    rating,
    description,
  } = restaurant;

  const res = await fetch("/api/restaurants", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name,
      address,
      cuisine_type,
      price_range,
      imageUrl,
      rating,
      description,
    }),
  });

  const data = await res.json();
  return data;
};

export const getUserRestaurantsThunk = () => async (dispatch) => {
  const res = await fetch("/api/restaurants/current");

  const data = await res.json();

  const normalizedData = {};
  Object.values(data.current_restaurants).forEach((restaurant) => {
    normalizedData[restaurant.id] = restaurant;
  });

  dispatch(readAllRestaurantsAction(normalizedData));
  return data;
};

export const deleteRestaurantThunk = (id) => async (dispatch) => {
  const res = await fetch(`/api/restaurants/${id}/delete`, {
    method: "DELETE",
  });

  const data = await res.json();

  dispatch(deleteRestaurantAction(id));

  return data;
};

const initialState = {
  singleRestaurant: {},
  allRestaurants: {},
};

const restaurantsReducer = (state = initialState, action) => {
  switch (action.type) {
    case GET_ALL_RESTAURANTS:
      return {
        ...state,
        allRestaurants: action.restaurants,
      };
    case GET_SINGLE_RESTAURANT:
      return {
        ...state,
        singleRestaurant: action.restaurant,
      };
    case DELETE_SINGLE_RESTAURANT:
      const newState = {
        ...state,
        allRestaurants: { ...state.allRestaurants },
      };
      delete newState.allRestaurants[action.id];
      return newState;
  }
};

export default restaurantsReducer;
