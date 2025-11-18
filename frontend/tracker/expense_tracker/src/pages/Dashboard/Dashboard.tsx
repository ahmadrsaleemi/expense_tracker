import React from "react";
import { useAuth } from "../../hooks/useAuth";

export default function Dashboard() {
  const { token } = useAuth();
  return (
    <div style={{ padding: "20px" }}>
      <h1>Dashboard</h1>
      <p>Welcome to expense tracker</p>
    </div>
  );
}
