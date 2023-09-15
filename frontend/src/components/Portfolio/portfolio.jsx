import React, { useEffect, useState, useRef } from "react";
import Chart from "chart.js/auto";

const SortableTable = () => {
	// Sample data for the table
	const [tableData, setTableData] = useState([
		{
			name: "Visa",
			symbol: "V",
			shares: 10,
			price: "$250",
			averageCost: "$200",
			return: "$500",
			equity: "$2,500",
		},
		{
			name: "Apple",
			symbol: "AAPL",
			shares: 10,
			price: "$150",
			averageCost: "$100",
			return: "$500",
			equity: "$1,500",
		},
		{
			name: "Amazon",
			symbol: "AMZN",
			shares: 150,
			price: "$100",
			averageCost: "$150",
			return: "$-50",
			equity: "$100",
		},
	]);

	const chartRef = useRef(null); // Create a ref to hold the chart instance

	const [highlightedIndex, setHighlightedIndex] = useState(null);

	useEffect(() => {
		// Define the chart configuration outside the effect
		const config = {
			type: "doughnut",
			data: {
				labels: ["Stock Symbol", "Equity"],
				datasets: [
					{
						data: [],
						backgroundColor: [
							"rgb(0, 200, 5)",
							"rgb(0, 200, 5)",
							"rgb(0, 200, 5)",
						],
						borderColor: ["white", "white", "white"],
						borderWidth: 3,
					},
				],
			},
			options: {
				responsive: false,
				maintainAspectRatio: false,
				plugins: {
					legend: false,
					tooltip: {
						enabled: false, // Disable the default tooltip
					},
				},
				cutout: "80%", // Adjust this value to control the size of the hole in the center
				onHover: (event, elements) => {
					if (elements.length > 0) {
						const hoveredElement = elements[0];
						const index = hoveredElement.index;
						setHighlightedIndex(index);
						updateDonutText(index);
					} else {
						setHighlightedIndex(null);
						updateDonutText(null);
					}
				},
			},
		};

		const ctx = document.getElementById("myDoughnutChart").getContext("2d");
		const myChart = new Chart(ctx, config);

		// Calculate the initial percentages based on the initial total equity
		const initialTotalEquity = tableData.reduce((acc, item) => {
			const equityValue = parseInt(
				item.equity.replace("$", "").replace(",", "")
			);
			return acc + equityValue;
		}, 0);

		const initialPercentages = tableData.map(item => {
			const equityValue = parseInt(
				item.equity.replace("$", "").replace(",", "")
			);
			return (equityValue / initialTotalEquity) * 100;
		});

		chartRef.current = myChart;
		chartRef.current.data.labels = ["Stock Symbol", "Equity"];
		chartRef.current.data.datasets[0].data = initialPercentages;
		chartRef.current.update();

		return () => {
			if (chartRef.current) {
				chartRef.current.destroy();
			}
		};
	}, []); // Empty dependency array means this effect runs once after the component is mounted

	// Sorting function
	const [sortOrder, setSortOrder] = useState(
		Array(tableData[0].length).fill(true)
	); // Initial sort order for each column

	const sortTable = column => {
		const newSortOrder = [...sortOrder];
		newSortOrder[column] = !newSortOrder[column];

		const newTableData = [...tableData];
		newTableData.sort((a, b) => {
			const cellA = a[Object.keys(a)[column]];
			const cellB = b[Object.keys(b)[column]];
			return newSortOrder[column]
				? cellA.localeCompare(cellB)
				: cellB.localeCompare(cellA);
		});

		setTableData(newTableData);
		setSortOrder(newSortOrder);
	};

	const updateDonutText = index => {
		if (chartRef.current) {
			if (index !== null) {
				const symbol = tableData[index].symbol;
				const equity = tableData[index].equity.replace("$", "");
				const equityValue = parseInt(equity);

				// Calculate the new percentages based on the initial total equity
				const percentages = tableData.map((item, i) => {
					return i === index
						? (equityValue / equityValue) * 100
						: (parseInt(item.equity.replace("$", "").replace(",", "")) /
								initialTotalEquity) *
								100;
				});

				chartRef.current.data.labels = [symbol, "Equity"];
				chartRef.current.data.datasets[0].data = percentages;
				chartRef.current.update();
			} else {
				// Reset the chart when no row is highlighted
				const initialPercentages = tableData.map(item => {
					const equityValue = parseInt(
						item.equity.replace("$", "").replace(",", "")
					);
					return (equityValue / initialTotalEquity) * 100;
				});

				chartRef.current.data.labels = ["Stock Symbol", "Equity"];
				chartRef.current.data.datasets[0].data = initialPercentages;
				chartRef.current.update();
			}
		}
	};

	return (
		<div className="container mx-auto mt-8 p-4 flex items-center">
			{/* Table Container */}
			<div className="w-1/2 table-container">
				<table className="table">
					<thead>
						<tr className="border-b">
							<th
								className="cursor-pointer border-green-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								onClick={() => sortTable(0)}>
								Name{" "}
								<span className="sort-icon">{sortOrder[0] ? "↓" : "↑"}</span>
							</th>
							<th
								className="cursor-pointer border-green-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								onClick={() => sortTable(1)}>
								Symbol{" "}
								<span className="sort-icon">{sortOrder[1] ? "↓" : "↑"}</span>
							</th>
							<th
								className="cursor-pointer border-green-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								onClick={() => sortTable(2)}>
								Shares{" "}
								<span className="sort-icon">{sortOrder[2] ? "↓" : "↑"}</span>
							</th>
							<th
								className="cursor-pointer border-green-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								onClick={() => sortTable(3)}>
								Price{" "}
								<span className="sort-icon">{sortOrder[3] ? "↓" : "↑"}</span>
							</th>
							<th
								className="cursor-pointer border-green-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								onClick={() => sortTable(4)}>
								Average cost{" "}
								<span className="sort-icon">{sortOrder[4] ? "↓" : "↑"}</span>
							</th>
							<th
								className="cursor-pointer border-green-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								onClick={() => sortTable(5)}>
								Total return{" "}
								<span className="sort-icon">{sortOrder[5] ? "↓" : "↑"}</span>
							</th>
							<th
								className="cursor-pointer border-green-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								onClick={() => sortTable(6)}>
								Equity{" "}
								<span className="sort-icon">{sortOrder[6] ? "↓" : "↑"}</span>
							</th>
						</tr>
					</thead>
					<tbody>
						{tableData.map((item, index) => (
							<tr
								key={index}
								className={`border-b border-gray-300 hover:bg-gray-100 ${
									index === highlightedIndex ? "bg-gray-200" : ""
								}`}
								onMouseEnter={() => {
									setHighlightedIndex(index);
									updateDonutText(index);
								}}
								onMouseLeave={() => {
									setHighlightedIndex(null);
									updateDonutText(null);
								}}>
								<td>{item.name}</td>
								<td>{item.symbol}</td>
								<td>{item.shares}</td>
								<td>{item.price}</td>
								<td>{item.averageCost}</td>
								<td>{item.return}</td>
								<td>{item.equity}</td>
							</tr>
						))}
					</tbody>
				</table>
			</div>

			{/* Donut Chart Container */}
			<div className="w-1/2 chart-container">
				<div className="bg-white border border-gray-300 rounded-lg shadow p-4">
					<canvas
						id="myDoughnutChart"
						width="200"
						height="200"></canvas>
					<div className="center-text">
						<div className="text-s font-semibold">
							{highlightedIndex !== null
								? tableData[highlightedIndex].symbol
								: "Stocks and Options"}
						</div>
						<div className="text-sm">
							Equity: $
							{highlightedIndex !== null
								? tableData[highlightedIndex].equity
								: tableData.reduce((acc, item) => {
										const equityValue = parseInt(
											item.equity.replace("$", "").replace(",", "")
										);
										return acc + equityValue;
								  }, 0)}
						</div>
					</div>
				</div>
			</div>
		</div>
	);
};

export default SortableTable;
