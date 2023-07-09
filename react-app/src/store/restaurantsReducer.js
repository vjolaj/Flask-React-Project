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

  //    if (res.ok) {
  //         const {restaurants} = await res.json();
  //         dispatch(readAllRestaurantsAction(restaurants));
  //     }
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

  //   const res = await fetch(`api/restaurants/${restaurantId}`)

  // if (res.ok){
  //   const restaurant = await res.json()
  //  dispatch(readSingleRestaurantAction(restaurant)); 
  //  return restaurant;
  // }
};


export const createRestaurantThunk = (restaurant) => async (dispatch) => {
  try {
    const res = await fetch("/api/restaurants/new", {
      method: "POST",
      body: restaurant,
    });

    if (res.ok) {
      const { resRestaurant } = await res.json();
      dispatch(readSingleRestaurantAction(resRestaurant));
    } else {
      const errorMessage = await res.text();
      throw new Error(errorMessage);
    }
  } catch (error) {
    console.log("Error creating restaurant:", error.message);
  }
};

export const editRestaurantThunk = (restaurant, restaurantId) => async (dispatch) => {
  try {
    const res = await fetch(`/api/restaurants/${restaurantId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: restaurant.name,
        address: restaurant.address,
        cuisineType: restaurant.cuisineType,
        priceRange: restaurant.priceRange,
        imageUrl: restaurant.imageUrl,
        description: restaurant.description
    })
    });

    if (res.ok) {
      const { resUpdatedRestaurant } = await res.json();
      dispatch(readSingleRestaurantAction(resUpdatedRestaurant));
    } else {
      const errorMessage = await res.text();
      throw new Error(errorMessage);
    }
  } catch (error) {
    console.log("Error updating restaurant:", error.message);
  }
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
    default:
      return state;
  }
};


export default restaurantsReducer;
