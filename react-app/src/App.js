import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch, useLocation} from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import LandingPage from "./components/LandingPage"
import RestaurantsIndex from "./components/RestaurantsIndex";

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
            <RestaurantsIndex/>
          </Route>
        </Switch>
      )}

      
    </>
  );
}

export default App;
