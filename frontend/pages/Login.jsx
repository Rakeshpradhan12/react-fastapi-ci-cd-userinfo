
import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { loginUserApi } from "../api/Auth"
import LoginForm from "../components/LoginForm"

const Login = () => {
    const navigate = useNavigate()
    const[loginData, setLoginData]=useState({
      username:'',
      password:''
    })
    const loginUser=async()=>{
      const data = await loginUserApi(
        loginData
      )
      if(data && data.access_token) {
        localStorage.setItem(
          'token',
          data.access_token
        )
        navigate('/dashboard')
      } else {
        alert('Login failed. Please check your credentials.')
      }
    }

    return (
      <LoginForm
      loginData={loginData}
      setLoginData={setLoginData}
      loginUser={loginUser}
      />
    )
}

export default Login