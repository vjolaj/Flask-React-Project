import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./NewRestaurant.css";
import {
  createRestaurantThunk,
  getUserRestaurantsThunk,
} from "../../store/restaurantsReducer";

export default function NewRestaurant() {
  const sessionUser = useSelector((state) => state.session.user);
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [cuisineType, setCuisineType] = useState("");
  const [priceRange, setPriceRange] = useState("");
  const [description, setDescription] = useState("");
  const [image, setImage] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [validationErrors, setValidationErrors] = useState({})
  const dispatch = useDispatch();
  const history = useHistory();
  const [submitted, setSubmitted] = useState(false)

  const cuisineTypes = [
    "",
    "American",
    "Asian",
    "Italian",
    "Mexican",
    "Seafood",
    "Pizza",
    "FastFood",
    "Sandwich",
    "Chinese",
    "Sushi",
    "Healthy",
  ];

  const prices = ["", "$", "$$", "$$$", "$$$$"];

  useEffect(() => {
    const errorsObject = {};
    if (!name) {
        errorsObject.name = "Name is required"
    }
    if (name.length > 255) {
       errorsObject.name = "Name can't be longer than 255 characters."
    }
    if (!address) {
        errorsObject.address = "Address is required"
    }
    if (address.length > 255) {
      errorsObject.address = "Address can't be longer than 255 characters."
    }
    if (!priceRange || priceRange === "") {
        errorsObject.priceRange = "Price range selection is required"
    }
    if (!cuisineType || cuisineType === "") {
        errorsObject.cuisineType = "Cuisine type selection is required"
    }
    if (!description) {
        errorsObject.description = "Description is required"
    }
    if (description.length > 255) {
      errorsObject.description = "Description can't be longer than 255 characters."
    }
    if (!image) {
        errorsObject.image = "Image upload is required"
    }

    setValidationErrors(errorsObject)
}, [name, address, priceRange, cuisineType, description, image])


  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitted(true)
    const formData = new FormData();
    formData.append("name", name);
    formData.append("address", address);
    formData.append("cuisineType", cuisineType);
    formData.append("priceRange", priceRange);
    formData.append("imageUrl", image);
    formData.append("description", description);
    // aws uploads can be a bit slow—displaying
    // some sort of loading message is a good idea
    setImageLoading(true);
    if (Object.values(validationErrors).length) {
      return null
  }
  setValidationErrors({})
    return dispatch(createRestaurantThunk(formData)).then(() => {
      dispatch(getUserRestaurantsThunk());
      history.push(`/restaurants/current`);
    });
  };

  return (
    <>
      <div className="add-restaurant-form">
        <form onSubmit={handleSubmit}>
          {/* <ul>
              {errors.map((error, idx) => (
                <li key={idx}>{error}</li>
              ))}
            </ul> */}
          <div className="formHeading">Add a new Restaurant</div>
          <div className="individualFormContainer">
            Enter a name for your restaurant
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
              placeholder="Restaurant Name"
              className="input"
              />
              {submitted && validationErrors.name && <p className="error">{validationErrors.name}</p>}
          </div>
          <div className="individualFormContainer">
            Enter the restaurant's address
            <input
              type="text"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
              placeholder="Restaurant Address"
              className="input"
            />
              {submitted && validationErrors.address && <p className="error">{validationErrors.address}</p>}

          </div>
          <div className="individualFormContainer cuisine">
            Select the restaurant's cuisine type
            <select
              value={cuisineType}
              onChange={(e) => setCuisineType(e.target.value)}
            >
              {cuisineTypes.map((cuisineType) => (
                <option key={cuisineType} value={cuisineType}>
                  {cuisineType}
                </option>
              ))}
            </select>
            {submitted && validationErrors.cuisineType && <p className="error">{validationErrors.cuisineType}</p>}

          </div>
          <div className="longerFormContainer">
            Select the restaurant's price range. If your entrees generally cost
            $1-10, select "$". If your entrees generally cost $11-20, select
            "$$". If your entrees generally cost $21-35, select "$$$". If your
            entrees generally cost more than $35, select "$$$$".
            <select
              value={priceRange}
              onChange={(e) => setPriceRange(e.target.value)}
            >
              {prices.map((price) => (
                <option key={price} value={price}>
                  {price}
                </option>
              ))}
            </select>
            {submitted && validationErrors.priceRange && <p className="error">{validationErrors.priceRange}</p>}
          </div>
          <div className="longerFormContainer">
            Please enter a description for your restaurant. Describe your
            cuisine and try to highlight what makes your restaurant unique.
            <input
              type="text"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
              placeholder="Restaurant Description"
              className="input"
            />
            {submitted && validationErrors.description && <p className="error">{validationErrors.description}</p>}
          </div>
          <div className="form-input-box">
            <div
              className="imageInputContainer longerFormContainer"
              htmlFor="image"
            >
              Post a preview image for your restaurant. This will appear on the
              landing page and on the individual restaurant page.
              <input
                id="image"
                type="file"
                accept="image/*"
                onChange={(e) => setImage(e.target.files[0])}
              ></input>
              {submitted && validationErrors.image && <p className="error">{validationErrors.image}</p>}

            </div>
          </div>
          <button type="submit" className="submit-form-button">
            Add your Restaurant
          </button>
        </form>
      </div>
    </>
  );
}
