import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { portfolioBaseURL } from "../util/baseUrl_api";

const initialState = {
	loading: false,
	portfolioInfo: null,
	error: "",
};

export const getPortfolio = createAsyncThunk(
	"portfolio/getPortfolio",
	async portfolioId => {
		const request = await axios.get(`${portfolioBaseURL}/${portfolioId}`);
		const response = await request.data;
		return response;
	}
);

export const portfolioSlice = createSlice({
	name: "portfolio",
	initialState,
	extraReducers: builder => {
		builder.addCase(getPortfolio.pending, state => {
			state.loading = true;
		});
		builder.addCase(getPortfolio.fulfilled, (state, action) => {
			state.loading = false;
			state.portfolioInfo = action.payload;
			state.error = "";
		});
		builder.addCase(getPortfolio.rejected, (state, action) => {
			state.loading = false;
			state.portfolioInfo = null;
			state.error = action.error.message;
		});
	},
});

export default portfolioSlice.reducer;
