import { Link } from 'react-router-dom'
import './LoginForm.css'

const LoginForm = ({
  loginData,
  setLoginData,
  loginUser
}) => {
  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2 className="auth-title">Login</h2>
        <div className="form-group">
          <input
            className="form-input"
            type='text'
            placeholder="Username"
            value={loginData.username}
            onChange={(e) => {
              setLoginData({
                ...loginData,
                username: e.target.value
              })
            }}
          />
        </div>
        <div className="form-group">
          <input
            className="form-input"
            type="password"
            placeholder="Password"
            value={loginData.password}
            onChange={(e) =>
              setLoginData({
                ...loginData,
                password: e.target.value,
              })
            }
          />
        </div>
        <button className="submit-btn" onClick={loginUser}>
          Login
        </button>
        <div className="auth-link">
          Don't have an account? <Link to="/register">Register here</Link>
        </div>
      </div>
    </div>
  )
}

export default LoginForm
