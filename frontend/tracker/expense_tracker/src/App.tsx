import "./App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import SignupPage from "./pages/Auth/SignupPage";
import LoginPage from "./pages/Auth/LoginPage";
import DashboardLayout from "./components/layout/DashboardLayout";
import Dashboard from "./pages/Dashboard/Dashboard";

import { useAuth } from "./hooks/useAuth";

const App = () => {
  const { token } = useAuth();
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signup" element={<SignupPage />} />
      <Route
        path="/dashboard"
        element={token ? <Dashboard /> : <Navigate to="/login" />}
      ></Route>
    </Routes>
  );
};

// function App() {
//   return (
//     <Routes>
//       <Route path="/signup" element={<SignupPage />} />
//       <Route path="/login" element={<LoginPage />} />
//       <Route
//         path="/dashboard"
//         element={token ? <Dashboard /> : <Navigate to="/login" />}
//       ></Route>
//     </Routes>
//   );
// }

export default App;
