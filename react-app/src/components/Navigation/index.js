import React, {useState, useEffect, useRef} from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import { removeFilter } from '../../store/filterReducer';
// import OpenModalButton from "../OpenModalButton";
import { useDispatch } from "react-redux";
// import { useHistory } from "react-router-dom";

import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	const dispatch = useDispatch();

  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

	  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleEpicEatsClick = () => {
    dispatch(removeFilter()); // Dispatch the removeFilter action
  };
	
	return (
		<div className='nav'>
			<div className='navLeft'>
				<div className='userButton'>
					<ProfileButton user={sessionUser} className='userButton'/>
				</div>
			<div className='logo'>
				<p>
					<NavLink exact to="/restaurants" className='logo' onClick={handleEpicEatsClick}>Epic</NavLink>
				</p>
				<p>
					<NavLink exact to="/restaurants" className='Eats' onClick={handleEpicEatsClick}>Eats</NavLink>
				</p>	
			</div>
				
			</div>
		</div>
		
	);
}

export default Navigation;