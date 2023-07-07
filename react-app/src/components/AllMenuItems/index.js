// import React, { useState, useEffect, useRef } from "react";
// import { useDispatch, useSelector } from "react-redux";
// import "./AllMenuItems.css";
// import { getAllMenuItemsThunk } from "../../store/menuItemsReducer";
// import { useParams } from "react-router-dom/cjs/react-router-dom.min";
// import ItemModal from "./itemModal";
// import { receiveFilter, removeFilter } from "../../store/filterReducer";

// export default function RestaurantMenuItems() {
//   const { restaurantId } = useParams();
//   const dispatch = useDispatch();
//   const menuItems = useSelector((state) => state.menuItems.allMenuItems);
//   const filter = useSelector((state) => state.filter.type);
//   const modalRef = useRef();

//   const [showMenu, setShowMenu] = useState(false);

//   const openMenu = (menuItem) => {
//     if (showMenu) return;
//     setShowMenu(true);
//   };

//   useEffect(() => {
//     if (!showMenu) return;

//     const closeMenu = (e) => {
//       if (!modalRef.current || !modalRef.current.contains(e.target)) {
//         setShowMenu(false);
//       }
//     };

//     document.addEventListener("click", closeMenu);

//     return () => document.removeEventListener("click", closeMenu);
//   }, [showMenu]);

//   useEffect(() => {
//     dispatch(getAllMenuItemsThunk(restaurantId));
//   }, [dispatch, restaurantId]);

//   const handleItemTypeChange = (itemType) => {
//       dispatch(receiveFilter(itemType));
//   };

//   if (!menuItems) {
//     return <div>Loading Menu Items...</div>;
//   }

//   const filteredMenuItems = filter ? Object.values(menuItems).filter((menuItem) => menuItem.itemType === filter): Object.values(menuItems);

//   return (
//     <div className="main-items">
//       <div className="item-type-filter">
//         <button
//           onClick={() => handleItemTypeChange(null)}
//           className={filter === null }
//         >
//           All
//         </button>
//         <button
//           onClick={() => handleItemTypeChange("Entree")}
//           className={filter === "Entree"}
//         >
//           Entrees
//         </button>
//         <button
//           onClick={() => handleItemTypeChange("Side")}
//           className={filter === "Side"}
//         >
//           Sides
//         </button>
//         <button
//           onClick={() => handleItemTypeChange("Dessert")}
//           className={filter === "Dessert"}
//         >
//           Desserts
//         </button>
//         <button
//           onClick={() => handleItemTypeChange("Drink")}
//           className={filter === "Drink"}
//         >
//           Beverages
//         </button>
//       </div>
//        <div className="menuItemsContainer">
//       {filteredMenuItems.length === 0 ? (
//         <div className="no-items-message">
//         </div>
//       ) : (
//         filteredMenuItems.map((menuItem) => (
//           <div className="itemContainer" key={menuItem.id}>
//             <div className="single-item-container">
//               <div>
//                 <img className="itemImage" src={menuItem.imageUrl} alt="image" />
//                 <ItemModal menuItem={menuItem} />
//                 <div className="itemImageContainer">
//                   <h1 className="plus">+</h1>
//                 </div>
//               </div>
//               <h3 className="itemName">{menuItem.itemName}</h3>
//               <div className="itemName">${menuItem.price}</div>
//             </div>
//           </div>
//         ))
//       )}
//     </div>
//     </div>
//   );
// }

import React, { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./AllMenuItems.css";
import { getAllMenuItemsThunk } from "../../store/menuItemsReducer";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import ItemModal from "./itemModal";
import { receiveFilter, removeFilter } from "../../store/filterReducer";

export default function RestaurantMenuItems() {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const menuItems = useSelector((state) => state.menuItems.allMenuItems);
  const filter = useSelector((state) => state.filter.type);
  const modalRef = useRef();

  const [showMenu, setShowMenu] = useState(false);

  const openMenu = (menuItem) => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!modalRef.current || !modalRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  useEffect(() => {
    dispatch(getAllMenuItemsThunk(restaurantId));
  }, [dispatch, restaurantId]);

  const handleItemTypeChange = (itemType) => {
    dispatch(receiveFilter(itemType));
  };

  if (!menuItems) {
    return <div>Loading Menu Items...</div>;
  }

  const filteredMenuItems = filter
    ? Object.values(menuItems).filter((menuItem) => menuItem.itemType === filter)
    : Object.values(menuItems);

  return (
    <div className="main-items">
      <div className="item-type-filter">
        <button
          onClick={() => handleItemTypeChange(null)}
          className={filter === null}
        >
          All
        </button>
        <button
          onClick={() => handleItemTypeChange("Entree")}
          className={filter === "Entree"}
        >
          Entrees
        </button>
        <button
          onClick={() => handleItemTypeChange("Side")}
          className={filter === "Side"}
        >
          Sides
        </button>
        <button
          onClick={() => handleItemTypeChange("Dessert")}
          className={filter === "Dessert"}
        >
          Desserts
        </button>
        <button
          onClick={() => handleItemTypeChange("Drink")}
          className={filter === "Drink"}
        >
          Beverages
        </button>
      </div>
      <div className="menuItemsContainer">
        {filteredMenuItems.length === 0 ? (
          <div className="no-items-message">
            Sorry, there are no {filter}s available at the moment.
          </div>
        ) : (
          filteredMenuItems.map((menuItem) => (
            <div className="itemContainer" key={menuItem.id}>
              <div className="single-item-container">
                <div>
                  <img className="itemImage" src={menuItem.imageUrl} alt="image" />
                  <ItemModal menuItem={menuItem} />
                  <div className="itemImageContainer">
                    <h1 className="plus">+</h1>
                  </div>
                </div>
                <h3 className="itemName">{menuItem.itemName}</h3>
                <div className="itemName">${menuItem.price}</div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
