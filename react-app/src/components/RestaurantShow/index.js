import React from 'react';
import { useParams } from 'react-router-dom';


const RestaurantShow = () =>{
    const { restaurantId } = useParams();

    return(
        <div>
            <h1>This is single restaurant page!</h1>
        </div>
    )
}

export default RestaurantShow