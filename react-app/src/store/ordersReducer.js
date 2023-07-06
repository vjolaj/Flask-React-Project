//constants
const GET_USER_ORDERS = '/user/orders/GET';
const POST_USER_ORDERS = '/user/orders/POST';
const GET_RESTAURANT_ORDERS = '/restaurants/orders/GET';
const EDIT_ORDER = '/order/PUT'

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

const EditOrder = (payload) => {
    return {
        type: EDIT_ORDER,
        payload
    }
}

//thunks
export const getUserOrdersThunk = () => async dispatch => {
    console.log('requesting from backend...')
    const res = await fetch('/api/orders/current'); //userId will be attached in the backend

    const data = await res.json();
    const normalizedData = {};
    Object.values(data.users_orders).forEach(order => {
        normalizedData[order.id] = order
    });

    dispatch(getUserOrdersAction(normalizedData));
    return data;
};

export const editOrderThunk = (id, body) => async dispatch => {
    const res = await fetch(`/api/orders/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    })
    if (res.ok) {
        const data = await res.json();
        dispatch(EditOrder(data))
    }
}

// export const checkoutThunk = (order) => async dispatch => {
//     const {  } = order

//     const res = await fetch('/api/orders', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({

//         })
//     })
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
        case EDIT_ORDER:
            return {
                ...state,
                cart: action.payload
            }
        default:
            return state;
    }
}

export default ordersReducer;
