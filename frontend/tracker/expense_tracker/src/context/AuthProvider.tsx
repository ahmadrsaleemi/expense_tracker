import React, { useState, ReactNode } from "react";
import { AuthContext } from "./AuthContext.tsx";

export const AuthProvider: React.FC<{ children: ReactNode }> = ({
  children,
}) => {
  const [token, setTokenState] = useState<string | null>(() =>
    localStorage.getItem("access_token")
  );

  const setToken = (token: string | null) => {
    if (token) localStorage.setItem("access_token", token);
    else localStorage.removeItem("access_token");
    setTokenState(token);
  };

  const logout = () => setToken(null);

  return (
    <AuthContext.Provider value={{ token, setToken, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
