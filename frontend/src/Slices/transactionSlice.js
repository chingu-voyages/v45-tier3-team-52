import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { transactionBaseURL } from "../util/baseUrl_api";

const initialState = {
	loading: false,
	transactionInfo: null,
	error: "",
};

// Generates pending, fulfilled, and rejected action types
export const getTransaction = createAsyncThunk(
	"transaction/getTransaction",
	async transactionId => {
		const request = await axios.get(`${transactionBaseURL}/${transactionId}`);
		const response = await request.data;
		return response;
	}
);
export const createTransaction = createAsyncThunk(
	"transaction/createTransaction",
	async transactionDetail => {
		const request = await axios.post(
			`${transactionBaseURL}/new`,
			transactionDetail
		);
		const response = await request.data;
		return response;
	}
);

export const updateTransaction = createAsyncThunk(
	"transaction/updateTransactionTransaction",
	async transactionDetail => {
		const request = await axios.put(
			`${transactionBaseURL}/new`,
			transactionDetail
		);
		const response = await request.data;
		return response;
	}
);

export const transactionSlice = createSlice({
	name: "transaction",
	initialState,
	extraReducers: builder => {
		builder
			.addMatcher(
				action => {
					return (
						action.type === getTransaction.pending.type ||
						action.type === createTransaction.pending.type
					);
				},
				state => {
					state.loading = true;
				}
			)
			.addMatcher(
				action => {
					return (
						action.type === getTransaction.fulfilled.type ||
						action.type === createTransaction.fulfilled.type
					);
				},
				(state, action) => {
					state.loading = false;
					state.transactionInfo = action.payload;
					state.error = "";
				}
			)
			.addMatcher(
				action => {
					return (
						action.type === getTransaction.rejected.type ||
						action.type === createTransaction.rejected.type
					);
				},
				(state, action) => {
					state.loading = false;
					state.transactionInfo = null;
					console.log(action.error.message);
					if (action.error.message === "Request failed with status code 401") {
						state.error = "This request can not be completed";
					} else {
						state.error = action.error.message;
					}
				}
			);
	},
});

export default transactionSlice.reducer;
