const BASE_URL = import.meta.env.VITE_BASE_URL;

// console.log(process.env.BASE_URL);

const registerUserApi =async (userData)=>{


  try{
    const response =
    await fetch(`${BASE_URL}/users`,
    {
      method :'POST',
      headers:{
        'content-type':'application/json',

      },
      body : JSON.stringify(userData)
    }
  )
  const resp = await response.json()
return resp
}
  catch(error){
    console.log(error)
  }
}

const loginUserApi = async(loginData)=>{
  const formData = new URLSearchParams();
  formData.append('username',loginData.username);
  formData.append('password',loginData.password);

  try{
  const response = await fetch(`${BASE_URL}/token`,
    {
      method: 'POST',
      headers:{
        'content-type':'application/x-www-form-urlencoded'
      },
      body:formData
    }
  )
  return response.json()
  }
  catch (error) {
    console.log(error)
  }

}

  const getProfileApi = async (token) => {
    try{
      const response = await fetch(
        `${BASE_URL}/users/me`,
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )
     return response.json()
    }
    catch(error){
      console.log(error)
    }

  }

const updateProfileApi=async ({token, updateData})=>{
  try{
    const response = await fetch(
      `${BASE_URL}/users/me`,
      {
        method:'PATCH',
        headers:{
          'content-type':'application/json',
          Authorization: `Bearer ${token}`
        },
        body:JSON.stringify(updateData)
  })

  return response.json()

}
catch(error){
  console.log(error)
}
}

export {registerUserApi, loginUserApi, getProfileApi, updateProfileApi}
