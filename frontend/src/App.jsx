import Splash from "./components/Splash/splash";
import AuthForm from "./components/Auth/auth_form";
import RegisterFormContainer from "./components/Auth/register_form_container";
import StockChartContainer from "./components/Stock/stockChart_container";
import ProfileContainer from "./components/Profile/profile_container";
import Portfolio from "./components/Portfolio/portfolio";
import { Routes, Route } from "react-router-dom";
import BuySellForm from "./components/BuySellForm/buysellform";
// import StockComponent from "./components/testing/StockComponent";
// import TransactionComponent from "./components/testing/TransactionComponent";
// import CreateTransactionForm from "./components/testing/CreateTransactionForm";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { authenticateUser } from "./Slices/authSlice";

function App() {
	const dispatch = useDispatch();

	// checks for an active user session (logged in user)
	useEffect(() => {
		const userId = localStorage.getItem("userId");
		(async () => {
			await dispatch(authenticateUser(Number(userId)));
		})();
	}, [dispatch]);
	const currentUser = useSelector(state => state.session.userInfo);
	console.log(currentUser);
	return (
		<div className="h-screen">
			<Routes>
				<Route
					exact
					path="/home"
					Component={StockChartContainer}
				/>
				<Route
					exact
					path="/profile"
					Component={ProfileContainer}
				/>

				<Route
					exact
					path="/portfolio"
					Component={Portfolio}
				/>
				<Route
					exact
					path="/login"
					Component={AuthForm}
				/>
				<Route
					exact
					path="/register"
					Component={RegisterFormContainer}
				/>
				<Route
					exact
					path="/"
					Component={Splash}
				/>
				<Route
					exact
					path="/stocks/:ticker"
					Component={BuySellForm}
				/>
			</Routes>
		</div>
	);
}

export default App;
