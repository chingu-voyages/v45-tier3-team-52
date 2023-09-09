import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTransaction } from "../Transaction/transactionSlice";

const TransactionComponent = () => {
	const dispatch = useDispatch();
	const transactionInfo = useSelector(
		state => state.transaction.transactionInfo
	);
	const loading = useSelector(state => state.transaction.loading);
	const error = useSelector(state => state.transaction.error);

	useEffect(() => {
		// Dispatch the getTransaction action with the provided transactionId when the component mounts
		dispatch(getTransaction(1));
	}, [dispatch]); // Ensure transactionId is included as a dependency

	return (
		<div>
			{loading ? (
				<p>Loading...</p>
			) : error ? (
				<p>Error: {error}</p>
			) : transactionInfo ? (
				<div>
					<h2>Transaction Info</h2>
					<p>User ID: {transactionInfo.userId}</p>
					<p>transactionInfo Status: {transactionInfo.status}</p>
					<p>transaction ID: {transactionInfo.id}</p>
					<ul>
						Stocks
						{transactionInfo.stocks.map((stock, index) => (
							<li key={index}>{stock.symbol}</li>
						))}
					</ul>
				</div>
			) : null}
		</div>
	);
};

export default TransactionComponent;
