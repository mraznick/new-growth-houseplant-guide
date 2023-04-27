import './App.css';
import { useState, useEffect } from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import Signup from './Screens/Signup';
import {getUser} from './services/users.js'

export default function App() {
  // const [user, setUser] = useState(null);
  // const [toggle, setToggle] = useState(false);

  // useEffect(() => {
  //   const fetchUser = async () => {
  //     let response = await getUser()
  //     setUser(response)
  //   }
  //   fetchUser()
  // }, [])

  return (
    <div className="newgrowth">
      <h1>Welcome to New Growth</h1>
      {/* <BrowserRouter>
        <Routes>
          <Route path="/register" element={<Signup setUser={setUser} />} />
          <Route path="/" element={<Home toggle={toggle} user={user} />} />
        </Routes>
      </BrowserRouter> */}
    </div>
  );
}


