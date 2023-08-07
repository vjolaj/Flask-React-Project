//constants
const GET_USER_ORDERS = '/user/orders/GET';
const POST_USER_ORDERS = '/user/orders/POST';
const GET_RESTAURANT_ORDERS = '/restaurants/orders/GET';
const ADD_TO_CART = '/user/cart/POST'
const GET_CART = '/user/cart/GET'
const EDIT_ORDER = '/order/edit'
const UPDATE_CART_ITEM = '/cart/item/PUT'

//action creators
const getUserOrdersAction = orders => {
    return {
        type: GET_USER_ORDERS,
        orders
    }
};

const setCartAction = cart => {
    return {
        type: GET_CART,
        cart
    }
}

const editOrderAction = order => {
    return {
        type: EDIT_ORDER,
        order
    }
}

const updateCartItemsAction = itemData => {
    return {
        type: UPDATE_CART_ITEM,
        itemData
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

    if (cartData.restaurantId >= 1) {
        const restaurantRes = await fetch(`/api/restaurants/${cartData.restaurantId}`)
        const restaurantData = await restaurantRes.json()
        cartData.restaurant = restaurantData.restaurant_info
    }

    dispatch(setCartAction(cartData))

    return cartData
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

export const checkOutCart = (id, data) => async dispatch => {
    const res = await fetch(`/api/orders/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            isCompleted: data.isCompleted,
            address: data.address,
            paymentDetails: data.paymentDetails,
            deliveryMethod: data.deliveryMethod,
            totalPrice: data.totalPrice
        })
    });
    const resData = await res.json()

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

export const addToCartThunk = (orderId, menuItemId, quantity) => async dispatch => {
    const res = await fetch(`/api/orders/${orderId}/menuItem`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            menuItemId,
            quantity
        })

    });
    const data = await res.json();

    const restaurantRes = await fetch(`/api/restaurants/${data.restaurantId}`)
    const restaurantData = await restaurantRes.json()
    data.restaurant = restaurantData.restaurant_info
    if (!res.ok) {
    }

    dispatch(setCartAction(data))

    return data
}

export const updateItemQuantityThunk = (quantity, orderId, menuItemId) => async dispatch => {
    const res = await fetch(`/api/orders/${orderId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            quantity,
            menuItemId,
            orderId,
            isCompleted: false
        })
    });

    const data = await res.json();
    dispatch(updateCartItemsAction(data.Items[menuItemId]))

    return data
};

export const deleteOrderItemThunk = (orderId, menuItemId) => async dispatch => {
    const res = await fetch(`/api/orders/${orderId}/menuItem`, {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            menuItemId
        })
    });

    const data = await res.json()

    if (Object.keys(data.Items).length !== 0) {
        const restaurantRes = await fetch(`/api/restaurants/${data.restaurantId}`)
        const restaurantData = await restaurantRes.json()
        data.restaurant = restaurantData.restaurant_info
    }

    dispatch(setCartAction(data))
    
    return data;
}

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
        case EDIT_ORDER:
            let newState;
            newState = { ...state}
            newState.currentUserOrders = { ...state.currentUserOrders };
            newState.currentUserOrders[action.order.id] = action.order;
            return newState;
        case UPDATE_CART_ITEM:
            return {
                ...state,
                cart: {
                    ...state.cart,
                    Items: {
                        ...state.cart.Items,
                        [action.itemData.id]: action.itemData 
                    }
                }
            }
        default:
            return state;
    }
}

export default ordersReducer;
