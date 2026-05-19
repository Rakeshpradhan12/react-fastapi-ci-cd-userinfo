import { useState, useEffect } from "react";
import UserProfile from '../components/UserProfile'
import UpdateProfile from "../components/UpdateProfile";
import { getProfileApi, updateProfileApi } from "../api/Auth";
import '../components/Dashboard.css'

const Dashboard=()=>{
  const token=localStorage.getItem('token')
  const[user, setUser]=useState(null)
  const[updateData, setUpdateData]=useState({
    name:'',
    email:''
  })
  useEffect(() => {
    const loadUser = async () => {
      const data = await getProfileApi(token)
      setUser(data)
    }

    loadUser()
  }, [token])

  const updateUser=async()=>{
    const data=await updateProfileApi({
      token,
      updateData
    })
    setUser(data)
    setUpdateData({ name: '', email: '' })
    alert('Profile updated successfully!')
  }

  const logout=()=>{
    localStorage.removeItem('token');
    window.location.href='/'
  }
if(!user){
  return (
    <div className="loading-container">
      <h1 className="loading-text">Loading...</h1>
    </div>
  )
}

return(
  <div className="dashboard-container">
    <div className="dashboard-header">
      <h1 className="dashboard-title">Dashboard</h1>
      <button className="logout-btn" onClick={logout}>Logout</button>
    </div>
    <div className="dashboard-content">
      <UserProfile user={user} logout={logout}/>
      <UpdateProfile
        updateData={updateData}
        setUpdateData={setUpdateData}
        updateUser={updateUser}
      />
    </div>
  </div>
)
}

export default Dashboard