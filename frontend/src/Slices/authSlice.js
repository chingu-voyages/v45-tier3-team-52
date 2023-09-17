import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { authBaseURL } from "../util/baseUrl_api";

const initialState = {
	loading: false,
	userInfo: null,
	userToken: null,
	error: "",
};

// * Login User
export const loginUser = createAsyncThunk(
	"auth/loginUser",
	async userCredentials => {
		const request = await axios.post(`${authBaseURL}/login`, userCredentials);
		const response = await request.data;
		return response;
	}
);
// * Logout User
export const logoutUser = createAsyncThunk("auth/logoutUser", async () => {
	axios.get(`${authBaseURL}/logout`);
});

// * Register User
export const registerUser = createAsyncThunk("auth/registerUser", async () => {
	const request = await axios.post(`${authBaseURL}/register`);
	const response = await request.data;
	console.log(response);
	return response;
});

// * Authenticate/ restore logged In user
export const authenticateUser = createAsyncThunk(
	"auth/authentication",
	async userId => {
		const request = await axios.get(`${authBaseURL}/${userId}`);
		const response = await request.data;
		return response;
	}
);

export const authSlice = createSlice({
	name: "auth",
	initialState,
	extraReducers: builder => {
		builder
			.addMatcher(
				action => {
					return (
						action.type === loginUser.pending.type ||
						action.type === logoutUser.pending.type ||
						action.type === authenticateUser.pending.type ||
						action.type === registerUser.pending.type
					);
				},
				state => {
					state.loading = true;
				}
			)
			.addMatcher(
				action => {
					return (
						action.type === loginUser.fulfilled.type ||
						action.type === logoutUser.fulfilled.type ||
						action.type === authenticateUser.fulfilled.type ||
						action.type === registerUser.fulfilled.type
					);
				},
				(state, action) => {
					state.loading = false;
					state.userInfo = action.payload;
					state.error = "";
					localStorage.setItem("userId", action.payload.id);
				}
			)
			.addMatcher(
				action => action.type === logoutUser.fulfilled.type,
				state => {
					state.loading = false;
					state.userInfo = {};
					state.error = "";
					localStorage.removeItem("userId");
				}
			)
			.addMatcher(
				action => {
					return (
						action.type === loginUser.rejected.type ||
						action.type === logoutUser.rejected.type ||
						action.type === authenticateUser.rejected.type ||
						action.type === registerUser.rejected.type
					);
				},
				(state, action) => {
					state.loading = false;
					state.userInfo = {};
					console.log(action.error.message);
					if (action.error.message === "Request failed with status code 401") {
						state.error = "Access Denied! Invalid Credentials";
					} else {
						state.error = action.error.message;
					}
				}
			);
	},
});

export default authSlice.reducer;
