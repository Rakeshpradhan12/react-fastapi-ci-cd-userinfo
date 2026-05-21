import './LoginForm.css'

const UpdateProfile = ({
  updateData,
  setUpdateData,
  updateUser
}) => {
  return (
    <div className="update-card">
      <h2 className="card-title">Update Profile</h2>
      <div className="form-group">
        <input
          className="form-input"
          type='text'
          placeholder="New Name"
          value={updateData.name}
          onChange={(e) => {
            setUpdateData({
              ...updateData,
              name: e.target.value
            })
          }}
        />
      </div>
      <div className="form-group">
        <input
          className="form-input"
          type="email"
          placeholder="New Email"
          value={updateData.email}
          onChange={(e) =>
            setUpdateData({
              ...updateData,
              email: e.target.value,
            })
          }
        />
      </div>
      <button className="submit-btn" onClick={updateUser}>
        Update
      </button>
    </div>
  )
}

export default UpdateProfile