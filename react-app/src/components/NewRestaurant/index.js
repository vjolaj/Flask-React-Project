import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import "./NewRestaurant.css";
import {
  createRestaurantThunk,
  getUserRestaurantsThunk,
} from "../../store/restaurantsReducer";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";

export default function NewRestaurant() {
  const sessionUser = useSelector((state) => state.session.user);
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [cuisineType, setCuisineType] = useState("");
  const [priceRange, setPriceRange] = useState("");
  const [description, setDescription] = useState("");
  const [image, setImage] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const dispatch = useDispatch();
  const history = useHistory();

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

  const handleSubmit = async (e) => {
    e.preventDefault();
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
