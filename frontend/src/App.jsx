import Splash from "./components/Splash/splash";
import AuthForm from "./components/Auth/auth_form";
import RegisterFormContainer from "./components/Auth/register_form_container";
import StockChartContainer from "./components/Stock/stockChart_container";
import ProfileContainer from "./components/Profile/profile_container";
import Portfolio from "./components/Portfolio/portfolio";
import { Routes, Route } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { authenticateUser } from "./Slices/authSlice";

function App() {
	const dispatch = useDispatch();
	const currentUser = useSelector(state => state.session.userInfo);

	// checks for an active user session (logged in user)
	useEffect(() => {
		const userId = localStorage.getItem("userId");
		if (userId) {
			const fetchUser = async () => {
				await dispatch(authenticateUser(userId));
			};
			fetchUser();
		}
	}, [dispatch]);
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
			</Routes>
		</div>
	);
}

export default App;
