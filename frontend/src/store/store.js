import { configureStore } from "@reduxjs/toolkit";
import authReducer from "../components/Auth/authSlice";
import stockReducer from "../components/Stock/stockSlice";
import transactionReducer from "../components/Transaction/transactionSlice";

export const store = configureStore({
	reducer: {
		session: authReducer,
		// profile: userReducer,
		stock: stockReducer,
		transaction: transactionReducer,
	},
});
