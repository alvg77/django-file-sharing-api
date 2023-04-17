import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  BrowserRouter,
} from "react-router-dom";
import './index.css'
import App from './App'

// const router = createBrowserRouter([
//   {
//     path: "/sign-in",
//     element: <SignIn />,
//     errorElement: <ErrorPage />,
//   },
//   {
//     path: "/sign-up",
//     element: <SignUp />,
//     errorElement: <ErrorPage />,
//   },

// ])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <RouterProvider router={router} /> */}
    <BrowserRouter >
      <App />
    </BrowserRouter>
  </React.StrictMode>,
)
