import axios from "axios";

export const register = user => axios.post("/api/auth/register", { user });
export const login = user => axios.post("/api/auth/login", { user });
export const logout = () => axios.delete("/api/auth/logout");
