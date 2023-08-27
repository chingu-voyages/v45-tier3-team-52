import SplashContainer from "./components/Splash/splash_container";
import LoginFormContainer from "./components/Auth/login_form_container";
import RegisterFormContainer from "./components/Auth/register_form_container";
import { Routes, Route } from "react-router-dom";

function App() {
	return (
		<div className="h-screen">
			<Routes>
				<Route
					exact
					path="/login"
					Component={LoginFormContainer}
				/>
				<Route
					exact
					path="/register"
					Component={RegisterFormContainer}
				/>
				<Route
					exact
					path="/"
					Component={SplashContainer}
				/>
			</Routes>
		</div>
	);
}

export default App;
