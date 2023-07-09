import React, { useState, useEffect } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { NavLink } from 'react-router-dom';
import { useHistory } from "react-router-dom";
import './LoginForm.css';
import { getCartThunk } from "../../store/ordersReducer";

function LoginFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const history = useHistory()

    useEffect(()=>{
        const errors = [];
        if (password.length > 1 || password.length < 6) errors.password="Password needs to be at least 6 characters.";
        setErrors(errors);
    },[password])


  if (sessionUser) return <Redirect to="/restaurants" />;

  
  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

   const demoUser = async (e) => {
    e.preventDefault()
    let email = "demo@aa.io"
    let password = "password"
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
      // dispatch(getCartThunk())
    } else {
      history.push("/restaurants")
    }
  }


  return (
    <>
   <div exact to="/" className='logIn-nav'>
				<p>
					<NavLink exact to="/" className='Epic-logIn-Nav'>Epic</NavLink>
				</p>
				<p>
					<NavLink exact to="/" className='Eats-logIn-Nav'>Eats</NavLink>
				</p>	
				</div>
        
      
      <form onSubmit={handleSubmit} className="logIn-Form">
        
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <label>
          <p>What's your email and password?</p>
         
          <input
          className="input"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            placeholder="Enter Email"
            
          />
        </label>
        <label>
        
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            placeholder="Enter Password"
            className="input"
          />
        </label>
        <button type="submit" className="logIn-form-button">Continue</button>
        <p className="or">or</p>
        <button type="button" onClick={demoUser} className="logIn-form-button">Continue with Demo User</button>
       
      </form>
     
    </>
  );
}

export default LoginFormPage;
