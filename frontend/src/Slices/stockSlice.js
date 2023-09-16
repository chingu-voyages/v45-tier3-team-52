import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { stockBaseURL } from "../util/baseUrl_api";

const initialState = {
	loading: false,
	stockInfo: null,
	error: "",
};

// Generates pending, fulfilled, and rejected action types
export const getStock = createAsyncThunk("stock/getStock", async stockId => {
	const request = await axios.get(`${stockBaseURL}/${stockId}`);
	const response = await request.data;
	return response;
});

export const stockSlice = createSlice({
	name: "stock",
	initialState,
	extraReducers: builder => {
		builder.addCase(getStock.pending, state => {
			state.loading = true;
		});
		builder.addCase(getStock.fulfilled, (state, action) => {
			state.loading = false;
			state.stockInfo = action.payload;
			state.error = "";
		});
		builder.addCase(getStock.rejected, (state, action) => {
			state.loading = false;
			state.stockInfo = null;
			state.error = action.error.message;
		});
	},
});

export default stockSlice.reducer;
