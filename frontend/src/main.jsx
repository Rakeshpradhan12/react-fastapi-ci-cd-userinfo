import { StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import {App} from './App.jsx'

// StrictMode helps detect:

// unsafe lifecycle methods
// side effects
// deprecated APIs
// accidental bugs

// It works only in development mode.
// useEffect runs twice
// API calls happen twice
// confusion during learning

ReactDOM.createRoot(document.getElementById('root'))
.render(
<StrictMode>
    <App />
</StrictMode>

)
