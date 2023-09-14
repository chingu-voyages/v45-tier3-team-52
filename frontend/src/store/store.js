import { configureStore } from "@reduxjs/toolkit";
import authReducer from "../components/Slices/authSlice";
import stockReducer from "../components/Slices/stockSlice";
import userReducer from "../components/Slices/userSlice";
import transactionReducer from "../components/slices/transactionSlice";
import portfolioReducer from "../components/Slices/portfolioSlice";

export const store = configureStore({
	reducer: {
		session: authReducer,
		portfolio: portfolioReducer,
		stock: stockReducer,
		transaction: transactionReducer,
		user: userReducer,
	},
});
