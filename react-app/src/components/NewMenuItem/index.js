import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import "./NewMenuItem.css";
import { addMenuItemThunk } from "../../store/menuItemsReducer";
import { useParams } from 'react-router-dom/cjs/react-router-dom.min'

function NewMenuItemPage() {
  const { restaurantId } = useParams();
  const sessionUser = useSelector((state) => state.session.user);
  const [itemName, setItemName] = useState("");
  const [price, setPrice] = useState("");
  const [image, setImage] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [itemType, setItemType] = useState("");
  const [description, setDescription] = useState("");
  const dispatch = useDispatch();
  const history = useHistory();
  const itemTypes = [
    "Side",
    "Entree",
    "Dessert",
    "Drink",
  ];
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("itemName", itemName);
    formData.append("price", price);
    formData.append("itemType", itemType);
    formData.append("description", description);
    formData.append("imageUrl", image);
    // aws uploads can be a bit slow—displaying
    // some sort of loading message is a good idea
    setImageLoading(true);
    return dispatch(addMenuItemThunk(restaurantId, formData))
    .then(() => {
        history.push(`/restaurants/${restaurantId}/menuitems`)
    })
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="addMenuItem-Form">
        {/* <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul> */}
        <p>Add a new menu item</p>
        <label>
          <input
            type="text"
            value={itemName}
            onChange={(e) => setItemName(e.target.value)}
            required
            placeholder="Enter Item Name"
            className="input"
          />
        </label>
        <label>
        Select the item category
        <select
          value = {itemType}
          onChange ={(e) => setItemType(e.target.value)}
        >
          {itemTypes.map(itemType => (
            <option
              key={itemType}
              value={itemType}
            >
              {itemType}
            </option>
          ))}
        </select>
      </label>
        <label>
          <input
            type="text"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            required
            placeholder="Enter price"
            className="input"
          />
        </label>
        <label>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
            placeholder="Item Description"
            className="input"
          />
        </label>
        <div className="form-input-box">
          <label className="form-label" htmlFor="image">
            Post Image:
          </label>
          <input
            id="image"
            type="file"
            accept="image/*"
            onChange={(e) => setImage(e.target.files[0])}
          ></input>
        </div>
        <button type="submit" className="submit-form-button">
          Add a new menu item
        </button>
      </form>
    </>
  );
}

export default NewMenuItemPage;