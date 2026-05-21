import { Link } from 'react-router-dom'
import './Home.css'

const Home = () => {
  return (
    <div className="home-container">
      <div className="hero-section">
        <h1 className="hero-title">Welcome to User Management System</h1>
        <p className="hero-subtitle">Manage your profile with ease and security</p>
        <div className="cta-buttons">
          <Link to="/login" className="btn btn-primary">Login</Link>
          <Link to="/register" className="btn btn-secondary">Register</Link>
        </div>
      </div>
      <div className="features">
        <div className="feature-card">
          <h3>🔒 Secure Authentication</h3>
          <p>JWT-based authentication for maximum security</p>
        </div>
        <div className="feature-card">
          <h3>👤 Profile Management</h3>
          <p>Update your profile information anytime</p>
        </div>
        <div className="feature-card">
          <h3>⚡ Fast & Reliable</h3>
          <p>Built with modern technologies for best performance</p>
        </div>
      </div>
    </div>
  )
}

export default Home
