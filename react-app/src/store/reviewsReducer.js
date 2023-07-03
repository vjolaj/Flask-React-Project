//constants
const GET_REVIEWS = 'reviews/restaurant/GET'
const POST_REVIEW = 'review/restaurant/GET';
const DELETE_REVIEW = '/review/restaurant/DELETE';

//action creators
const getRestaurantReviewsAction = reviews => {
    return {
        type: GET_REVIEWS,
        reviews
    }
};

const createRestaurantReviewAction = review => {
    return {
        type: POST_REVIEW,
        review
    }
};

const deleteReviewAction = id => {
    return {
        type: DELETE_REVIEW,
        id
    }
}

//thunks
export const getRestaurantReviewsThunk = (restaurantId) => async dispatch => {
    const res = await fetch(`/api/restaurant/${restaurantId}/reviews`);

    const data = await res.json();

    const normalizedData = {};
    Object.values(data.Reviews).forEach(review => {
        normalizedData[review.id] = review
    });
    
    dispatch(getRestaurantReviewsAction(normalizedData));
    return data;
};

export const createRestaurantReviewThunk = (review) => async dispatch => {
    const { restaurantId, description, rating } = review;

    const res = await fetch(`/api/spots/${restaurantId}/reviews`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            description,
            rating
        })
    });
    
    const data = await res.json();
    
    if (res.ok) {
        dispatch(createRestaurantReviewAction(data)) 
        // dispatch(getSingleRestaurantThunk(id)) 
    }
    return data;
};

export const deleteReviewThunk = (id, spotId) => async dispatch => {
    const res = await fetch(`/api/reviews/${id}`, {
        method: 'DELETE'
    })

    const data = await res.json();

    if (res.ok) {
        dispatch(deleteReviewAction(id))
        // dispatch(getSingleSpotThunk(spotId))
    }

    return data;
}

const initialState = {
    restaurant: {},
    user: {}
};

const reviewsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_REVIEWS:
            return {
                ...state,
                spot: action.reviews
            };
            case POST_REVIEW:
                const newState = {...state,
                restaurant: {...state.restaurant
                }};
                newState.restaurant[action.review.id] = action.review
                return newState;
            case DELETE_REVIEW:
                const newState1 = {
                    ...state,
                    restaurant: {...state.restaurant}
                };
                delete newState.restaurant[action.id]
                return newState1;

        default:
            return state;
    }
}

export default reviewsReducer;
