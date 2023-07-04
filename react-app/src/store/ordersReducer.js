//constants
const GET_USER_ORDERS = '/user/orders/GET';
const POST_USER_ORDERS = '/user/orders/POST';
const GET_RESTAURANT_ORDERS = '/restaurants/orders/GET';

//action creators
const getUserOrdersAction = orders => {
    return {
        type: GET_USER_ORDERS,
        orders
    }
};

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

//thunks
const getUserOrdersThunk = () => async dispatch => {
    const res = await fetch('/api/orders/current'); //userId will be attached in the backend

    const data = await res.json();
    const normalizedData = {};
    Object.values(data.Orders).forEach(order => {
        normalizedData[order.id] = order
    });

    dispatch(getUserOrdersAction(normalizedData));
    return data;
};

const postUserOrderThunk = (order) => async dispatch => {
    const {  } = order

    const res = await fetch('/api/orders', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({

        })
    })
}

const initialState = {
    currentUserOrders: {},
    restaurantOrders: {}
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
            newState.currentUserOrders[action.order.id] = action.order
            return newUserOrders;
        case GET_RESTAURANT_ORDERS:
            return {
                ...state,
                restaurantOrders: action.orders
            };
    }
}