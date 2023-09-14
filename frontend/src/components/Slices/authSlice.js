import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { authBaseURL } from "../../util/baseUrl_api";

const initialState = {
	loading: false,
	userInfo: null,
	userToken: null,
	error: "",
};

// Generates pending, fulfilled, and rejected action types
export const loginUser = createAsyncThunk(
	"auth/loginUser",
	async userCredentials => {
		const request = await axios.post(`${authBaseURL}/login`, userCredentials);
		const response = await request.data;
		return response;
	}
);

export const logoutUser = createAsyncThunk("auth/logoutUser", () => {
	axios.get(`${authBaseURL}/logout`).then(res => res.data);
});

export const authSlice = createSlice({
	name: "auth",
	initialState,
	extraReducers: builder => {
		builder
			.addMatcher(
				action => {
					return (
						action.type === loginUser.pending.type ||
						action.type === logoutUser.pending.type
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
						action.type === logoutUser.fulfilled.type
					);
				},
				(state, action) => {
					state.loading = false;
					state.userInfo =
						action.type === loginUser.fulfilled.type ? action.payload : {};
					state.error = "";
				}
			)
			.addMatcher(
				action => {
					return (
						action.type === loginUser.rejected.type ||
						action.type === logoutUser.rejected.type
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
