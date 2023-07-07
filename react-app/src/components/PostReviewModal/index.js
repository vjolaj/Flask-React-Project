import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import StarsRatingInput from "./StarsRating";
import { readSingleRestaurantThunk } from "../../store/restaurantsReducer";
import { createRestaurantReviewThunk, getRestaurantReviewsThunk } from "../../store/reviewsReducer";
import './Review.css'

function ReviewModal({ restaurant }) {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [description, setDescription] = useState("");
  const [rating, setRating] = useState(0);
  const [errors, setErrors] = useState({});
  const [errorRes, setErrorRes] = useState({});

  useEffect(() => {
    const err = {};
    if (description.length < 10 && description.length > 1) err.description = 'Review must be between 10 and 250 characters';
    if(description.length === 0) err.description ='';
    if (description.length > 250) err.description = 'Sorry your review is too long';
    if (rating < 1) err.rating = '';
    setErrors(err);
  }, [description, rating]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors({});
    const newReview = {
      rating,
      description
    };
    const addReviewRes = await dispatch(createRestaurantReviewThunk(newReview, restaurant.id));
    if (addReviewRes.message) {
      await setErrorRes(addReviewRes);
    }
    await closeModal();
    await dispatch(getRestaurantReviewsThunk(restaurant.id));
    await dispatch(readSingleRestaurantThunk(restaurant.id));
  };

  const onChange = (rating) => {
    setRating(parseInt(rating));
  };

  return (
    <>
      <div className="reviewContainer">
        <form className="reviewForm" onSubmit={handleSubmit}>
          <h1>Tell us how we did!</h1>
          {Boolean(Object.values(errors).length) && (
            <div className="errorContainer">
              {Object.values(errors).map((errorMsg, index) => (
                <p key={index} className="error">{errorMsg}</p>
              ))}
            </div>
          )}
          <textarea
            cols='40'
            rows='7'
            placeholder="Leave your review here..."
            value={description}
            name="review"
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
          <div className="starsContainer">
            <StarsRatingInput disabled={false} onChange={onChange} rating={rating} />
            <p>Stars</p>
          </div>
          <button type="submit" className="submitReview" disabled={Boolean(Object.values(errors).length)}>Submit</button>
        </form>
      </div>
    </>
  );
}

export default ReviewModal;





