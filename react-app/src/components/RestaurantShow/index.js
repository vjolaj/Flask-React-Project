import React from "react";
import { useParams } from "react-router-dom";
import RestaurantMenuItems from "../AllMenuItems";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { readSingleRestaurantThunk } from "../../store/restaurantsReducer";
import { getAllMenuItemsThunk } from "../../store/menuItemsReducer";
import NewMenuItemModal from "../NewMenuItemModal";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import { getRestaurantReviewsThunk } from "../../store/reviewsReducer";
import "./restaurantShow.css";
import OpenModalButton from "../OpenModalButton";


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

  // console.log(reviews, '😍')
  // console.log(restaurant);
  // console.log(menuItems)

  // Calculate total number of reviews
  const totalReviews = reviews.length;

  // Calculate average rating
  const averageRating =
    totalReviews > 0
      ? reviews.reduce((sum, review) => sum + review.rating, 0) / totalReviews
      : NaN;

   const reviewNum = (num) => {
        if (num === 1) return "1 rating"
        else return ` ${num} ratings`
    }

  useEffect(() => {
    dispatch(readSingleRestaurantThunk(restaurantId));
    dispatch(getAllMenuItemsThunk(restaurantId));
    dispatch(getRestaurantReviewsThunk(restaurantId));
  }, [dispatch, restaurantId]);

  if (!restaurant || !menuItems || !reviews) return null;

  const filteredMenuItems = Object.values(menuItems).filter(
    (menuItem) => menuItem.restaurantId === restaurantId
  );

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
              <p>{averageRating}</p>
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
            {/* <p>This is your Restaurant!</p> */}
            {/* <NavLink to={`/restaurants/${restaurant.id}/newmenuitem`}> */}
              {/* <button>Add more items to your Menu!</button> */}
              {/* <img src="https://cdn-icons-png.flaticon.com/512/43/43869.png"  alt="plus" className="plus"/> */}
             {/* <button className="click-here">Click here to add more items</button> */}
             <OpenModalButton
                buttonText="Add a Menu Item"
                modalComponent={<NewMenuItemModal restaurant={restaurant} />}
              />
            {/* </NavLink> */}
            {/* </div> */}
          </div>
        )}
      </div>

      <div>
        <div>
          <h2>Rating & Reviews</h2>
          {reviews.length > 0 ? (
            <ul>
              {reviews.map((review) => (
                <li key={review.id}>
                  <h3>{review.UserName}</h3>
                  {[...Array(review.rating)].map((_, index) => (
                    <i key={index} className="fa-solid fa-star"></i>
                  ))}
                  <p>{review.description}</p>
                </li>
              ))}
            </ul>
          ) : (
            <p>No reviews found.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default RestaurantShow;
