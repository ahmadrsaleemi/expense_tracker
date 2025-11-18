import { React } from "react";
import { Link } from "react-router-dom";
import "./assets/css/Sidebar.css";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>My App</h2>
      <nav>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/products">Products</Link>
        <Link to="/store">Store</Link>
        <Link to="/stats">Stats</Link>
        <Link to="/profile">Profile</Link>
      </nav>
    </div>
  );
};

export default Sidebar;
