import React from "react";
import { useAuth } from "../../hooks/useAuth";

const Topbar = () => {
  const { logout } = useAuth();
  return (
    <div className="topbar">
      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default Topbar;
