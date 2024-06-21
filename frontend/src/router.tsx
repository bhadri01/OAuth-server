import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Home from "./pages/home";
import Signup from "./pages/signup";
import Login from "./pages/login";

export const router = createBrowserRouter([
    {
      path: '/',
      element: <App />,
      children: [
        { path: '/', element: <Home /> },
        { path: 'signup', element: <Signup /> },
        { path: 'login', element: <Login /> },
      ],
    },
  ]);