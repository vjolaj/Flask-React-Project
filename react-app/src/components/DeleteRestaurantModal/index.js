import { useDispatch, useSelector } from "react-redux";
import { useState } from 'react';
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useModal } from "../../context/Modal";
import './DeleteRestaurantModal.css'
import { deleteRestaurantThunk } from "../../store/restaurantsReducer";
import { getUserRestaurantsThunk } from "../../store/restaurantsReducer";

function DeleteRestaurantModal ({restaurant}) {
    const { closeModal } = useModal();
    const dispatch = useDispatch();
    const history = useHistory();

    const handleSubmit = (e) => {
        e.preventDefault();
        // setErrors({});
        return dispatch(deleteRestaurantThunk(restaurant.id))
        .then(() => {
          closeModal();
          dispatch(getUserRestaurantsThunk())
        //   })
        //   .catch(async (res) => {
        //     const data = await res.json();
        //     if (data && data.errors) {
        //       setErrors(data.errors);
        //     }
        }
          );
      };

    return (
        <div className="deleteRestaurant">
            <div className="deleteHeader">Confirm Delete</div>
            <div className="deleteText">Are you sure you want to remove this spot from your listings?</div>
            <div>
                <button
                id="yesDelete"
                onClick={handleSubmit}
                >
                    Yes (Delete Restaurant)
                </button>
                <button
                id="noDelete"
                onClick={((e) => {
                  closeModal();
                  e.stopPropagation();
                  history.push('/restaurants/current')
                  })}
                >
                    No (Keep Restaurant)
                </button>
            </div>
        </div>
    )
}

export default DeleteRestaurantModal;