import React from "react";
import { useAuth } from "../../hooks/useAuth";
import DashboardLayout from "../../components/layout/DashboardLayout.tsx";

export default function Dashboard() {
  return (
    <DashboardLayout>
      <h1>Dashboard</h1>
      <p>Welcome to your dashboard.</p>
    </DashboardLayout>
  );
}
