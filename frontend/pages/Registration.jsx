import {useState } from "react";
import { useNavigate } from "react-router-dom";
import RegisterForm from "../components/RegisterForm";
import { registerUserApi } from "../api/Auth";



const Registration = () => {
  const navigate = useNavigate()
  const [formData, setFormData]=
  useState({
    name:'',
    email:'',
    password:''
  })
  const registerUser = async () => {
    const response = await registerUserApi(formData)
    if(response) {
      alert('Registered successfully! Please login.')
      navigate('/login')
    }
  }

  return (
    <RegisterForm
      formData={formData}
      setFormData={setFormData}
      registerUser={registerUser}
    />
  )

}
export default Registration