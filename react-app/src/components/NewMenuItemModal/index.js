import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import "./NewMenuItemModal.css";
import { addMenuItemThunk, getAllMenuItemsThunk} from "../../store/menuItemsReducer";
import {readSingleRestaurantThunk } from "../../store/restaurantsReducer";
import { getRestaurantReviewsThunk } from "../../store/reviewsReducer";
import { useParams } from 'react-router-dom/cjs/react-router-dom.min'
import { useModal } from "../../context/Modal";

function NewMenuItemModal({restaurant}) {
  // const { restaurantId } = useParams();
  const { closeModal } = useModal();
  const sessionUser = useSelector((state) => state.session.user);
  const [itemName, setItemName] = useState("");
  const [price, setPrice] = useState("");
  const [image, setImage] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [itemType, setItemType] = useState("");
  const [description, setDescription] = useState("");
  const dispatch = useDispatch();
  const history = useHistory();
  const [validationErrors, setValidationErrors] = useState({})
  const [submitted, setSubmitted] = useState(false)
  const itemTypes = [
    "",
    "Side",
    "Entree",
    "Dessert",
    "Drink",
  ];

  useEffect(() => {
    const errorsObject = {};
    if (!itemName) {
        errorsObject.itemName = "Item name is required"
    }
    if (itemName.length > 255) {
      errorsObject.itemName = "Item name can't be longer than 255 characters."
  }
    if (!price) {
        errorsObject.price = "Price is required"
    }
    if (isNaN(price) || Number(price) < 0 || Number(price) > 99.99) {
        errorsObject.price = "Item price must be a numeric value between 0.00 and 99.99"
    }
    if (!itemType || itemType === "") {
        errorsObject.itemType = "Item type selection is required"
    }
    if (!description) {
        errorsObject.description = "Description is required"
    }
    if (description.length > 255) {
      errorsObject.description = "Item description can't be longer than 255 characters."
  }
    if (!image) {
        errorsObject.image = "Image upload is required"
    }

    setValidationErrors(errorsObject)
}, [itemName, price, itemType, description, image])

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitted(true)
    const formData = new FormData();
    formData.append("itemName", itemName);
    formData.append("price", price);
    formData.append("itemType", itemType);
    formData.append("description", description);
    formData.append("imageUrl", image);
    // aws uploads can be a bit slow—displaying
    // some sort of loading message is a good idea
    setImageLoading(true);
    if (Object.values(validationErrors).length) {
      return null
    }
    setValidationErrors({})
    return dispatch(addMenuItemThunk(restaurant.id, formData))
    .then(() => {
        closeModal();
        dispatch(readSingleRestaurantThunk(restaurant.id));
    dispatch(getAllMenuItemsThunk(restaurant.id));
    dispatch(getRestaurantReviewsThunk(restaurant.id));
        history.push(`/restaurants/${restaurant.id}`)
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
        <h2>New item details</h2>
        <label>
          <input
            type="text"
            value={itemName}
            onChange={(e) => setItemName(e.target.value)}
            required
            placeholder="Enter Item Name"
            className="input"
          />
          {submitted && validationErrors.itemName && <p className="error">{validationErrors.itemName}</p>}
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
        {submitted && validationErrors.itemType && <p className="error">{validationErrors.itemType}</p>}
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
          {submitted && validationErrors.price && <p className="error">{validationErrors.price}</p>}
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
          {submitted && validationErrors.description && <p className="error">{validationErrors.description}</p>}
        </label>
        <div className="form-input-box">
          <label className="file-upload-button" htmlFor="image">
            Post Image: 
          </label>
          <input
            id="image"
            type="file"
            accept="image/*"
            onChange={(e) => setImage(e.target.files[0])}
          ></input>
          {submitted && validationErrors.image && <p className="error">{validationErrors.image}</p>}
        </div>
        <button type="submit" className="submit-new-item">
          Add to the menu
        </button>
      </form>
    </>
  );
}

export default NewMenuItemModal;