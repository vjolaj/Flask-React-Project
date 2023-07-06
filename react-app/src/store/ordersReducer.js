//constants
const GET_USER_ORDERS = '/user/orders/GET';
const POST_USER_ORDERS = '/user/orders/POST';
const GET_RESTAURANT_ORDERS = '/restaurants/orders/GET';
const ADD_TO_CART = '/user/cart/POST'
const GET_CART = '/user/cart/GET'

//action creators
const getUserOrdersAction = orders => {
    return {
        type: GET_USER_ORDERS,
        orders
    }
};

const addToCartAction = menuItem => {
    return {
        type: ADD_TO_CART,
        menuItem
    }
}

const postUserOrderAction = order => {
    return {
        type: POST_USER_ORDERS,
        order
    }
};

const getRestaurantsOrders = orders => {
    return {
        type: GET_RESTAURANT_ORDERS,
        orders
    }
};

const setCartAction = cart => {
    return {
        type: GET_CART,
        cart
    }
}

//thunks
export const getUserOrdersThunk = () => async dispatch => {
    const res = await fetch('/api/orders/current'); //userId will be attached in the backend

    const data = await res.json();
    const normalizedData = {};
    Object.values(data.users_orders).forEach(order => {
        normalizedData[order.id] = order
    });

    dispatch(getUserOrdersAction(normalizedData));
    return data;
};

export const getCartThunk = () => async dispatch => {
    const cartRes = await fetch("/api/cart")
	const cartData = await cartRes.json()

    dispatch(setCartAction(cartData))

    return null
}

export const newCartThunk = () => async dispatch => {
    const cartRes = await fetch("/api/cart/new-order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });
    const cartData = await cartRes.json();

    dispatch(setCartAction(cartData))

    return null
}

// export const addToCartThunk = (menuItem) => async dispatch => {

//     const res = await fetch(`/api/orders/${}`)
// }


const initialState = {
    currentUserOrders: {},
    restaurantOrders: {},
    cart: {}
}

const ordersReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_USER_ORDERS:
            return {
                ...state,
                currentUserOrders: action.orders
            }
        case POST_USER_ORDERS:
            const newUserOrders = {
                ...state,
                currentUserOrders: {...state.currentUserOrders}
            };
            newUserOrders.currentUserOrders[action.order.id] = action.order
            return newUserOrders;
        case GET_RESTAURANT_ORDERS:
            return {
                ...state,
                restaurantOrders: action.orders
            };
        case GET_CART:
            return {
                ...state,
                cart: action.cart
            }
        default:
            return state;
    }
}

export default ordersReducer;
