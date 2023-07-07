import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import "./EditRestaurant.css"
import { readSingleRestaurantThunk, getUserRestaurantsThunk, editRestaurantThunk } from "../../store/restaurantsReducer";
import { useParams } from 'react-router-dom/cjs/react-router-dom.min'

export default function EditRestaurant() {
  const { restaurantId } = useParams();
    const sessionUser = useSelector((state) => state.session.user);
    const restaurant = useSelector(
      (state) => state.restaurants.allRestaurants[restaurantId]
    );
    const [name, setName] = useState("");
    const [address, setAddress] = useState("")
    const [cuisineType, setCuisineType] = useState("")
    const [priceRange, setPriceRange] = useState("")
    const [description, setDescription] = useState("")
    const [image, setImage] = useState(null);
    const [imageLoading, setImageLoading] = useState(false);
    const [validationErrors, setValidationErrors] = useState({})
    const [submitted, setSubmitted] = useState(false)
    const dispatch = useDispatch();
    const history = useHistory();

    const cuisineTypes = [
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
        "Healthy"
    ]

    const prices = [
        "$",
        "$$",
        "$$$",
        "$$$$"
    ]

    useEffect(() => {
      const errorsObject = {};
      if (!name) {
          errorsObject.name = "Name is required"
      }
      if (!address) {
          errorsObject.address = "Address is required"
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
      if (!image) {
          errorsObject.image = "Image upload is required"
      }
  
      setValidationErrors(errorsObject)
  }, [name, address, priceRange, cuisineType, description, image])

    useEffect(() => {
      if (restaurant) {
        setName(restaurant.name || "");
        setAddress(restaurant.address || "");
        setCuisineType(restaurant.cuisineType || "");
        setDescription(restaurant.description || "");
        setPriceRange(restaurant.priceRange || "");
        setImage(restaurant.imageUrl.filename || "");
      }
    }, [restaurant]);

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
        return dispatch(editRestaurantThunk(formData, restaurantId)).then(() => {
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
            <div className="formHeading">Edit Your Restaurant</div>
            <div className="individualFormContainer">
              Edit the name of your restaurant
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
                Edit the restaurant's address
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
            Edit the restaurant's cuisine type
            <select
              value = {cuisineType}
              onChange ={(e) => setCuisineType(e.target.value)}
            >
              {cuisineTypes.map(cuisineType => (
                <option
                  key={cuisineType}
                  value={cuisineType}
                >
                  {cuisineType}
                </option>
              ))}
            </select>
            {submitted && validationErrors.cuisineType && <p className="error">{validationErrors.cuisineType}</p>}
          </div>
          <div className="longerFormContainer">
            Edit the restaurant's price range. If your entrees generally cost $1-10, select "$". If your entrees generally cost $11-20, select "$$". If your entrees generally cost $21-35, select "$$$". If your entrees generally cost more than $35, select "$$$$".
            <select
              value = {priceRange}
              onChange ={(e) => setPriceRange(e.target.value)}
            >
              {prices.map(price => (
                <option
                  key={price}
                  value={price}
                >
                  {price}
                </option>
              ))}
            </select>
            {submitted && validationErrors.priceRange && <p className="error">{validationErrors.priceRange}</p>}
          </div>
            <div className="longerFormContainer">
            Edit the description for your restaurant. Describe your cuisine and try to highlight what makes your restaurant unique.
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
              <div className="imageInputContainer longerFormContainer" htmlFor="image">
                Post a new preview image for your restaurant. This will appear on the landing page and on the individual restaurant page.
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
              Edit Your Restaurant
            </button>
          </form>
          </div>
        </>
      );
}