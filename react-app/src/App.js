import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch, useLocation} from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import LandingPage from "./components/LandingPage"
import RestaurantsIndex from "./components/RestaurantsIndex";
import RestaurantMenuItems from "./components/AllMenuItems";
import RestaurantShow from "./components/RestaurantShow";
import Main from "./components/Main";
import CheckoutPage from "./components/CheckoutPage.js";
import NewRestaurant from "./components/NewRestaurant";
import ManageRestaurants from "./components/ManageRestaurants";
import PastOrdersPage from "./components/Orders/pastOrders";
import EditRestaurant from "./components/EditRestaurant";
import Footer from "./components/Footer"
import CheckOutModal from "./components/CheckoutPage.js/checkoutModal";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const location = useLocation();

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  const hideNavigation = location.pathname === '/login' || location.pathname === "/signup";

  return (
    <>
      <div className="content-wrap">
      {!hideNavigation && < Navigation isLoaded={isLoaded}/>}
        {isLoaded && (
          <Switch>
            <Route exact path = '/'>
              <LandingPage/>
            </Route>
            <Route path="/login" >
              <LoginFormPage />
            </Route>
            <Route path="/signup">
              <SignupFormPage />
            </Route>
            <Route exact path='/restaurants'>
              <Main/>
            </Route>
            <Route exact path='/restaurants/current'>
              <ManageRestaurants/>
            </Route>
            <Route exact path='/restaurants/newrestaurant'>
              <NewRestaurant/>
            </Route>
            <Route exact path = "/restaurants/:restaurantId/menuitems">
              <RestaurantMenuItems />
            </Route>
            <Route exact path='/restaurants/:restaurantId/update'>
              <EditRestaurant />
            </Route>
            <Route exact path='/restaurants/:restaurantId'>
              <RestaurantShow/>
            </Route>
            <Route exact path='/user/checkout'>
              <CheckoutPage/>
            </Route>
            <Route exact path='/orders'>
              <PastOrdersPage />
            </Route>
            <Route exact path='/finalizing-checkout'>
              <CheckOutModal />
            </Route>
          </Switch>
        )}
      </div>
      <Footer/>

    </>
  );
}

export default App;
