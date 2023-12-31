const ADD_MENU_ITEM = "/restaurant/menuitems/new";
const GET_ALL_MENU_ITEMS = "/restaurants/menuitems/all";
const CLEAR_ITEMS = 'items/clear'

const readAllMenuItemsAction = (menuItems) => {
  return {
    type: GET_ALL_MENU_ITEMS,
    menuItems,
  };
};

export const addMenuItem = (menuItem) => {
    return {
        type: ADD_MENU_ITEM,
        menuItem,
    }    
}

export const clearItemsAction = () =>{
    return {
        type: CLEAR_ITEMS
    }
}


//thunks
export const getAllMenuItemsThunk = (restaurantId) => async (dispatch) => {
  const res = await fetch(`/api/restaurants/${restaurantId}/menu-items`);

  const data = await res.json();
  const normalizedData = {};
  Object.values(data.restaurant_menu_items).forEach((menuItem) => {
    normalizedData[menuItem.id] = menuItem;
  });

  dispatch(readAllMenuItemsAction(normalizedData));
  return data;
};

export const addMenuItemThunk = (id, menuItem) => async (dispatch) => {
  const res = await fetch(`/api/restaurants/${id}/menu-items`, {
    method: "POST",
    body: menuItem,
  });

  if (res.ok) {
    const { resMenuItem } = await res.json();
    dispatch(addMenuItem(resMenuItem));
  } else {
  }
};

const initialState = {
  singleMenuItem: {},
  allMenuItems: {},
};

const menuItemsReducer = (state = initialState, action) => {
let newState;
  switch (action.type) {
    case GET_ALL_MENU_ITEMS:
      return {
        ...state,
        allMenuItems: action.menuItems,
      };
    case ADD_MENU_ITEM:
        return {
            ...state,
            allMenuItems: action.menuItems,
          };
    case CLEAR_ITEMS:
      return{...state, singleMenuItem:{}}
    default:
      return state;
  }
};

export default menuItemsReducer;