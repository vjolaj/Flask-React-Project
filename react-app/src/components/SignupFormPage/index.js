import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import { NavLink } from 'react-router-dom';
import './SignupForm.css';

function SignupFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("")
	const [lastName, setLastName] = useState("")
	const [phoneNumber, setPhoneNumber] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/restaurants" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password === confirmPassword) {
        const data = await dispatch(signUp(username, email, password, firstName, lastName, phoneNumber));
        if (data) {
          setErrors(data)
        }
    } else {
        setErrors(['Confirm Password field must be the same as the Password field']);
    }
  };

  return (
    <>
      <div className='logIn-nav'>
				<p>
					<NavLink exact to="/" className='Epic-logIn-Nav'>Epic</NavLink>
				</p>
				<p>
					<NavLink exact to="/" className='Eats-logIn-Nav'>Eats</NavLink>
				</p>	
				</div>
  
      
      <form onSubmit={handleSubmit} className="logIn-Form">

        <ul>
          {errors.map((error, idx) => <li key={idx}>{error}</li>)}
        </ul>
        <p>Join Epic Eats today</p>
        <label>
         
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            placeholder="Enter Email"
            className="input"
          />
        </label>
        	<label>
		  		<input
						type="integer"
						value={phoneNumber}
						onChange={(e) => setPhoneNumber(e.target.value)}
						required
            placeholder="Enter Phone Number"
            className="input"
					/>
				</label>
        <label>
         
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            placeholder="Username"
            className="input"
          />
        </label>
        <label>
					<input
						type="text"
						value={firstName}
						onChange={(e) => setFirstName(e.target.value)}
						required
            placeholder="First Name"
            className="input"
					/>
				</label>
				<label>
					<input
						type="text"
						value={lastName}
						onChange={(e) => setLastName(e.target.value)}
						required
            placeholder="Last Name"
            className="input"
					/>
				</label>
        <label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            placeholder="Password"
            className="input"
          />
        </label>
        <label>
         
          <input
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
            placeholder="Confirm Password"
            className="input"
          />
        </label>
        <button type="submit" className="logIn-form-button">Sign Up</button>
      </form>
    </>
  );
}

export default SignupFormPage;
