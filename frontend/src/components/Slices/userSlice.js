import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { userBaseURL } from "../../util/baseUrl_api";

const initialState = {
	loading: false,
	userInfo: null,
	error: "",
};

//TODO: need to pull userId somewhere in session
export const getUser = createAsyncThunk("user/getUser", async userId => {
	const request = await axios.get(`${userBaseURL}/${userId}`);
	const response = await request.data;
	return response;
});

export const userSlice = createSlice({
	name: "user",
	initialState,
	extraReducers: builder => {
		builder.addCase(getUser.pending, state => {
			state.loading = true;
		});
		builder.addCase(getUser.fulfilled, (state, action) => {
			state.loading = false;
			state.userInfo = action.payload;
			state.error = "";
		});
		builder.addCase(getUser.rejected, (state, action) => {
			state.loading = false;
			state.userInfo = null;
			state.error = action.error.message;
		});
	},
});

export default userSlice.reducer;
