export const RECEIVE_FILTER = "RECEIVE_FILTER"
export const REMOVE_FILTER = "REMOVE_FILTER"

export const receiveFilter = filter => {
    return {
        type: RECEIVE_FILTER,
        filter
    }
}

export const removeFilter = () => {
    return {
        type: REMOVE_FILTER
    }
}

const filterReducer = (state = {}, action) => {
    Object.freeze(state)
    const nextState = Object.assign({}, state)

    switch (action.type) {
        case RECEIVE_FILTER:
            return  Object.assign({}, state, {type: action.filter})
        case REMOVE_FILTER:
            return {}
        default:
            return state;
    }

}

export default filterReducer