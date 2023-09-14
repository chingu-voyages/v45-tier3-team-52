import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { userBaseURL } from "../../util/baseUrl_api";

const initialState = {
	loading: false,
	userInfo: null,
	error: "",
};

export const updateUser = createAsyncThunk("user/updateUser", async data => {
	const request = await axios.put(`${userBaseURL}/${data.id}`, data);
	const response = await request.data;
	return response;
});

export const userSlice = createSlice({
	name: "user",
	initialState,
	extraReducers: builder => {
		builder.addCase(updateUser.pending, state => {
			state.loading = true;
		});
		builder.addCase(updateUser.fulfilled, (state, action) => {
			state.loading = false;
			state.userInfo = action.payload;
			state.error = "";
		});
		builder.addCase(updateUser.rejected, (state, action) => {
			state.loading = false;
			state.userInfo = null;
			state.error = action.error.message;
		});
	},
});

export default userSlice.reducer;
