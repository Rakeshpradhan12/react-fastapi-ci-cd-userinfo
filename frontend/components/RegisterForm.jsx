import { Link } from 'react-router-dom'
import './LoginForm.css'

export default function RegisterForm({
  formData,
  setFormData,
  registerUser,
}) {
  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2 className="auth-title">Register</h2>
        <div className="form-group">
          <input
            className="form-input"
            type='text'
            placeholder="Name"
            value={formData.name}
            onChange={(e) => {
              setFormData({
                ...formData,
                name: e.target.value
              })
            }}
          />
        </div>
        <div className="form-group">
          <input
            className="form-input"
            type="email"
            placeholder="Email"
            value={formData.email}
            onChange={(e) =>
              setFormData({
                ...formData,
                email: e.target.value,
              })
            }
          />
        </div>
        <div className="form-group">
          <input
            className="form-input"
            type="password"
            placeholder="Password"
            value={formData.password}
            onChange={(e) =>
              setFormData({
                ...formData,
                password: e.target.value,
              })
            }
          />
        </div>
        <button className="submit-btn" onClick={registerUser}>
          Register
        </button>
        <div className="auth-link">
          Already have an account? <Link to="/login">Login here</Link>
        </div>
      </div>
    </div>
  );
}
