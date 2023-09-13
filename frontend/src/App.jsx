import Splash from "./components/Splash/splash";
import AuthForm from "./components/Auth/auth_form";
import RegisterFormContainer from "./components/Auth/register_form_container";
import StockChartContainer from "./components/Stock/stockChart_container";
import { Routes, Route } from "react-router-dom";

function App() {
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
					path="/login"
					Component={AuthForm}
				/>
				<Route
					exact
					path="/register"
					Component={RegisterFormContainer}
				/>
				{/* <Route
					exact
					path="/transaction/new"
					Component={CreateTransactionForm}
				/> */}
				{/* <Route
					exact
					path="/stock"
					Component={StockComponent}
				/>
				<Route
					exact
					path="/transaction"
					Component={TransactionComponent}
				/> */}
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
