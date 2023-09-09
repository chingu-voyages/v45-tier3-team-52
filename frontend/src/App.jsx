import Splash from "./components/Splash/splash";
import AuthForm from "./components/Auth/auth_form";
import Login from "./components/testing/Login";
// import RegisterFormContainer from "./components/Auth/register_form_container";
import StockChartContainer from "./components/Stock/stockChart_container";
import { Routes, Route } from "react-router-dom";
import BuySellForm from "./components/BuySellForm/buysellform";
import StockComponent from "./components/testing/StockComponent";
import TransactionComponent from "./components/testing/TransactionComponent";
import CreateTransactionForm from "./components/testing/CreateTransactionForm";

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
				{/* <Route
					exact
					path="/register"
					Component={RegisterFormContainer}
				/> */}
				<Route
					exact
					path="/transaction/new"
					Component={CreateTransactionForm}
				/>
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
				<Route
					exact
					path="/buy"
					Component={BuySellForm}
				/>
			</Routes>
		</div>
	);
}

export default App;
