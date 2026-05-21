import './Dashboard.css'

const UserProfile = ({ user, logout }) => {
  return (
    <div className="profile-card">
      <h2 className="card-title">User Profile</h2>
      <div className="profile-info">
        <div className="info-row">
          <span className="info-label">ID:</span>
          <span className="info-value">{user.id}</span>
        </div>
        <div className="info-row">
          <span className="info-label">Name:</span>
          <span className="info-value">{user.name}</span>
        </div>
        <div className="info-row">
          <span className="info-label">Email:</span>
          <span className="info-value">{user.email}</span>
        </div>
      </div>
    </div>
  )
}

export default UserProfile
