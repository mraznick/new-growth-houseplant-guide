import { useState, useRef } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { registerUser, getUser } from '../services/users.js';

export default function Signup({ setUser }) {
  const [formData, setFormData] = useState({
    "username": "",
    "password": "",
    "re_password": "",
    "email": "",
  })

  let navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    await registerUser(formData)
    let response = await getUser
    setUser(response)
    navigate("/")
  }

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }))
  }

  return (
    <div className="signup-container">
      <h1 className="main-header">New Growth</h1>
      <h5 className="subheader">Find the right plants for you based on your lifestyle!</h5>
      <div class="signup-box">
        <h2>Sign Up</h2>
        <form onSubmit={handleSubmit} class="register-login-form">
          <input
            type="text"
            placeholder="What's your name?"
            name="username"
            value={formData.username}
            onChange={handleChange}
          />
          <br />
          <input
            type="text"
            placeholder="What's your email?"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
          <br />
          <input
            type="password"
            placeholder="Set a password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
          <br />
          <input
            type="password"
            placeholder="Confirm password"
            name="re_password"
            value={formData.re_password}
            onChange={handleChange}
          />
          <br />
          <button type="submit">Submit</button>
        </form>
        <nav className="signup">
          <div>Already have an account? <Link to='/signin'><a id="my-profile-link" className="nav-auth">Login Here</a></Link>
          </div>
        </nav>
      </div>
    </div>
  )
}