import {BrowserRouter, Routes, Route} from "react-router-dom"
import Home from "../pages/Home"
import Login from "../pages/Login"
import Dashboard from "../pages/Dashboard"
import Registration from "../pages/Registration"

 const AppRouter= ()=>{
  return(
    <BrowserRouter>
      <Routes>
        <Route
        path='/'
        element={<Home/>}
        />
        <Route
        path='/login'
        element={<Login/>}
        />
        <Route
          path='/dashboard'
          element={<Dashboard />}
        />
        <Route
          path='/register'
          element={<Registration />}
        />
      </Routes>
    </BrowserRouter>

  )

}

export default AppRouter