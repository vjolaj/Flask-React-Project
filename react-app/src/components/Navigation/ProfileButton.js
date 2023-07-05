import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
// import OpenModalButton from "../OpenModalButton";
// import LoginFormModal from "../LoginFormModal";
// import SignupFormModal from "../SignupFormModal";
// import { NavLink } from 'react-router-dom';
import { useHistory } from "react-router-dom";
import './Navigation.css'

function ProfileButton({ user }) {
  const history = useHistory();
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;


    const closeMenu = (e) => {
      if (!ulRef.current || !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);
  const closeMenu = () => setShowMenu(false);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push('/');
    closeMenu()
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  

    const loginButton = (e) => {
        e.preventDefault();
        history.push('/login')
        closeMenu();
    }

    const signupButton = (e) => {
        e.preventDefault();
        history.push('/signup')
        closeMenu();
    }
  const ordersRedirect = (e) => {
    e.preventDefault();
    history.push('/orders')
    closeMenu()
  }
  return (
    <>
      <button onClick={openMenu} className="userButton">
        <i className="fa-solid fa-bars fa-2xl"></i>
      </button>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <li>{user.username}</li>
            <li>{user.email}</li>
            <li onClick={ordersRedirect}>Past Orders</li>
            <li>
              <button onClick={handleLogout}>Log Out</button>
            </li>
          </>
        ) : (
          <>
            {/* <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            /> */}
        <div className="menuButtons">
          <button onClick={signupButton} className="menuSignUpButton">Sign Up</button>
          <button onClick={loginButton} className="menuLoginButton">Log in</button>
          
        </div>
        

            {/* <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            /> */}
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
