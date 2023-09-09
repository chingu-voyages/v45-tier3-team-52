import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getStock } from "../Stock/stockSlice";

const StockComponent = () => {
	const dispatch = useDispatch();
	const stockInfo = useSelector(state => state.stock.stockInfo);
	const loading = useSelector(state => state.stock.loading);
	const error = useSelector(state => state.stock.error);

	useEffect(() => {
		dispatch(getStock(2));
	}, [dispatch]);

	return (
		<div>
			{loading ? (
				<p>Loading...</p>
			) : error ? (
				<p>Error: {error}</p>
			) : stockInfo ? (
				<div>
					<h2 className="font-extrabold text-4xl underline">Stock Info</h2>
					<p className="font-bold text-2xl text-blue-800">
						Stock Name: {stockInfo.org_name}
					</p>
					<p className="font-bold text-xl text-green-700">
						Stock Name: {stockInfo.symbol}
					</p>
					<p className="font-bold text-lg text-red-600">
						Stock Price: {stockInfo.current_price}
					</p>
				</div>
			) : null}
		</div>
	);
};

export default StockComponent;
