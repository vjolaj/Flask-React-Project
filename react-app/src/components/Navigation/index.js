import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className='nav'>
			<div className='navLeft'>
				<p className='userButton'>
					<ProfileButton user={sessionUser} className='userButton'/>
				</p>
				<div className='logo'>
				<p>
					<NavLink exact to="/" className='logo'>Epic</NavLink>
				</p>
				<p>
					<NavLink exact to="/" className='Eats'>Eats</NavLink>
				</p>	
				</div>
				
			</div>

			<div></div>

		</div>
		
	);
}

export default Navigation;