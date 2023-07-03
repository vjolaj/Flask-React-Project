// import { NavLink } from "react-router-dom";
// import { useSelector, useDispatch } from "react-redux";
import React from "react";
import "./landing.css";
import { useHistory } from "react-router-dom";
// import ProfileButton from "../Navigation/ProfileButton";
// import { clearPageAction } from "../../store/session";
// import { useEffect } from "react";
// import { useDispatch, useSelector } from 'react-redux';

const LandingPage = () => {
  const history = useHistory();
  // const dispatch = useDispatch();
  // const sessionUser = useSelector(state => state.session.user);
  // const [showMenu, setShowMenu] = useState(false);

    // const closeMenu = () => setShowMenu(false);

    const loginButton = (e) => {
        e.preventDefault();
        history.push('/login')
        // closeMenu();
    }

    const signupButton = (e) => {
        e.preventDefault();
        history.push('/signup')
        // closeMenu();
    }

    // useEffect(()=>{
    //   return (() => dispatch(clearPageAction()))
    // },[dispatch])
  return (
    <>

      <div className="landingBack">
        <div className="landing-nav-right">
           <button onClick={loginButton} className="whiteLogIn">Log in</button>
          <button onClick={signupButton} className="blackSignUp">Sign Up</button>
        </div>

        <h1 className="orderFood">Order food to your Door</h1>
        <img
          className="main-bg"
          src="https://oobreats.s3.amazonaws.com/splash6.webp"
          alt=""
        />
      </div>
    </>
  );
};

export default LandingPage;
