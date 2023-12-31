import { getAllMenuItemsThunk } from "./menuItemsReducer";
import { getCartThunk, newCartThunk } from "./ordersReducer";
import { getAllRestaurantsThunk, readSingleRestaurantThunk } from "./restaurantsReducer";
import { getRestaurantReviewsThunk } from "./reviewsReducer";

// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
// const CLEAR_PAGE = 'page/clear'

const setUser = (user) => ({
	type: SET_USER,
	user
});

const removeUser = () => ({
	type: REMOVE_USER,
});

// export const clearPageAction = () =>{
//     return {
//         type: CLEAR_PAGE
//     }
// };

const initialState = {
	user: null,
};

export const authenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
		dispatch(getCartThunk())
		dispatch(readSingleRestaurantThunk())
		dispatch(getAllRestaurantsThunk())
		// dispatch(getRestaurantReviewsThunk())
		// dispatch(getAllMenuItemsThunk())
	}
};

export const login = (email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			email,
			password,
		}),
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		const cart = await dispatch(getCartThunk())
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

export const logout = () => async (dispatch) => {
	const response = await fetch("/api/auth/logout", {
		headers: {
			"Content-Type": "application/json",
		},
	});

	if (response.ok) {
		dispatch(removeUser());
	}
};

export const signUp = (username, email, password, firstName, lastName, phoneNumber) => async (dispatch) => {
	const response = await fetch("/api/auth/signup", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			username,
			email,
			password,
			firstName,
			lastName,
			phoneNumber
		}),
	});

	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		dispatch(newCartThunk())
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

export default function reducer(state = initialState, action) {
	switch (action.type) {
		case SET_USER:
			return { user: action.user };
		case REMOVE_USER:
			return { user: null};
		// case CLEAR_PAGE:
		// 	return{...state, initialState:{}}
		default:
			return state;
	}
}
