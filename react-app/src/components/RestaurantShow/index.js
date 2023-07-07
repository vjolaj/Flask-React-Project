import React from "react";
import { useParams } from "react-router-dom";
import RestaurantMenuItems from "../AllMenuItems";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { readSingleRestaurantThunk } from "../../store/restaurantsReducer";
import { getAllMenuItemsThunk } from "../../store/menuItemsReducer";
import NewMenuItemModal from "../NewMenuItemModal";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import {getRestaurantReviewsThunk} from "../../store/reviewsReducer";
import "./restaurantShow.css";
import OpenModalButton from "../OpenModalButton";
import ReviewModal from "../PostReviewModal";
import DeleteReviewModal from "../DeleteReviewModal";

const RestaurantShow = () => {
  const { restaurantId } = useParams();
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const restaurant = useSelector(
    (state) => state.restaurants.allRestaurants[restaurantId]
  );
  const menuItems = useSelector((state) => state.menuItems.allMenuItems);
  let reviews = useSelector((state) => state.reviews.reviews);
  reviews = Object.values(reviews);

  // Calculate total number of reviews
  const totalReviews = reviews.length;

  // Calculate average rating
  const averageRating =
    totalReviews > 0
      ? reviews.reduce((sum, review) => sum + review.rating, 0) / totalReviews
      : NaN;

  const reviewNum = (num) => {
    if (num === 1) return "1 rating";
    else return ` ${num} ratings`;
  };

  useEffect(() => {
    dispatch(readSingleRestaurantThunk(restaurantId));
    dispatch(getAllMenuItemsThunk(restaurantId));
    dispatch(getRestaurantReviewsThunk(restaurantId));
  }, [dispatch, restaurantId]);

  if (!restaurant || !menuItems || !reviews) return null;

  const filteredMenuItems = Object.values(menuItems).filter(
    (menuItem) => menuItem.restaurantId === restaurantId
  );

  const postReviewButton = (user, reviews, restaurant) => {
    if (user === null || user === undefined) return false; //=> Need to log in to post a review
    // for (let review of reviews) {
    //     if (review.userId === user.id) // =>Can't post a second review
    //         return false;
    // }
    // if (user.id === restaurant.ownerId) return false;// => You can't write a review for your own spot
    return true;
  };

  const deleteReviewButton = (user, review) => {
    if (user === null || user === undefined) return false;
    if (user.id === review.userId) return true;
    return false;
  };

  return (
    <div>
      <img src={restaurant.imageUrl} alt="img" className="rest-img" />
      <div className="name-address-container">
        <h1 className="rest-tittle">
          {restaurant.name} ({restaurant.address})
        </h1>
        <div className="restaurant-details">
          <i className="fa-solid fa-star"></i>
          {isNaN(averageRating) ? (
            <p>New!</p>
          ) : (
            <>
              <p>{Number.parseFloat(averageRating).toFixed(1)}</p>
              <p>({reviewNum(totalReviews)})</p>
            </>
          )}
          <p>• {restaurant.cuisineType} •</p>
          <p>{restaurant.priceRange}</p>
        </div>
        <p className="delivery">30-45 min • $3.99 Delivery Fee</p>
      </div>

      <RestaurantMenuItems menuItems={filteredMenuItems} />
      <div>
        {user && restaurant.ownerId === user.id && (
          <div className="plus-container"> 
           <OpenModalButton
              buttonText="Add a Menu Item"
              modalComponent={<NewMenuItemModal restaurant={restaurant} />}
            />
          </div>
        )}
      </div>

      <div>
        <div className="rating-and-reviews">
          <h2>Rating & Reviews</h2>
          <div className="newReview">
            {postReviewButton(user, reviews, restaurant) ? (
              <OpenModalButton
                buttonText="Add new Review"
                modalComponent={<ReviewModal restaurant={restaurant} />}
              />
            ) : null}
          </div>
          {reviews.length > 0 ? (
            <ul>
              <div className="review-container">
                {reviews.map((review) => (
                  <div key={review.id}>
                    <div className="single-review-container">
                      <h4>{review.UserName}</h4>
                      {[...Array(5)].map((_, i) => (
                        <i
                          key={i}
                          className={`fa-solid fa-star ${
                            i < review.rating ? "filled" : "empty"
                          }`}
                        ></i>
                      ))}
                      <p>{review.description}</p>

                      {deleteReviewButton(user, review) ? (
                        <OpenModalButton
                          buttonText="Delete"
                          modalComponent={
                            <DeleteReviewModal
                              review={review}
                              restaurantId={restaurantId}
                            />
                          }
                        />
                      ) : null}
                    </div>
                  </div>
                ))}
              </div>
            </ul>
          ) : (
            <p></p>
          )}
        </div>
      </div>
    </div>
  );
};

export default RestaurantShow;
