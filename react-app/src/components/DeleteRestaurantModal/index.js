import { useDispatch } from "react-redux";
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
          history.push('/restaurants/current')
        }
          );
      };

    return (
        <div className="mainContainer">
            <div className="deleteText">
            <h1 className="h1Delete">Confirm Delete</h1>
            <p className="pDelete">Are you sure you want to remove this restaurant ?</p>  
            </div>
        
            <div className="YN">
                <button
                className="Ybutton"
                id="yesDelete"
                onClick={handleSubmit}
                >
                    Yes (Delete Restaurant)
                </button>
                <button
                className="Nbutton"
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