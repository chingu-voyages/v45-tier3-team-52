import { configureStore } from "@reduxjs/toolkit";
import authReducer from "../Slices/authSlice";
import stockReducer from "../Slices/stockSlice";
import transactionReducer from "../Slices/transactionSlice";
import portfolioReducer from "../Slices/portfolioSlice";

export const store = configureStore({
	reducer: {
		session: authReducer,
		portfolio: portfolioReducer,
		stock: stockReducer,
		transaction: transactionReducer,
	},
});
