import { useState } from "react";
import { useDispatch } from "react-redux";
import { createTransaction } from "../Transaction/transactionSlice";

const CreateTransactionForm = () => {
	const dispatch = useDispatch();
	const [formData, setFormData] = useState({
		userId: "",
		stocks: [],
	});

	const handleChange = e => {
		const { name, value } = e.target;

		// Special handling for stocks (assuming it's an array of strings)
		if (name === "stocks") {
			const selectedStocks = Array.from(
				e.target.selectedOptions,
				option => option.value
			);
			setFormData({ ...formData, [name]: selectedStocks });
		} else {
			setFormData({ ...formData, [name]: value });
		}
	};

	const handleSubmit = e => {
		e.preventDefault();

		// Dispatch the createTransaction action with formData
		dispatch(createTransaction(formData));
	};

	return (
		<div>
			<h2>Create Transaction</h2>
			<form onSubmit={handleSubmit}>
				<div>
					<label htmlFor="userId">User ID:</label>
					<input
						type="text"
						id="userId"
						name="userId"
						value={formData.userId}
						onChange={handleChange}
					/>
				</div>
				<div>
					<label htmlFor="stocks">Stocks:</label>
					<select
						multiple
						id="stocks"
						name="stocks"
						value={formData.stocks}
						onChange={handleChange}>
						{/* Assuming you have a list of available stocks */}
						<option value={1}>Stock ID 1</option>
						<option value={2}>Stock ID 2</option>
						<option value={3}>Stock ID 3</option>
						{/* Add more options as needed */}
					</select>
				</div>
				<button type="submit">Create Transaction</button>
			</form>
		</div>
	);
};

export default CreateTransactionForm;
