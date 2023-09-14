import React, { useState } from "react";

const textInputStyle = "text-s font-bold";
const inputStyle =
	"border-solid border-gray-300 border w-full mt-2 py-1 px-2 rounded text-black";

const Profile = () => {
	return (
		<div className="container mx-auto mt-8 p-4 flex items-center">
			<div className="w-1/2 table-container">
				<table className="table">
					<thead>
						<tr>
							<th
								className="cursor-pointer border-gray-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								id="nameHeader">
								Name
								<span className="sort-icon">&darr;</span>
							</th>
							<th
								className="cursor-pointer border-gray-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								id="symbolHeader">
								Symbol
								<span className="sort-icon">&darr;</span>
							</th>
							<th
								className="cursor-pointer border-gray-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								id="sharesHeader">
								Shares
								<span className="sort-icon">&darr;</span>
							</th>
							<th
								className="cursor-pointer border-gray-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								id="priceHeader">
								Price
								<span className="sort-icon">&darr;</span>
							</th>
							<th
								className="cursor-pointer border-gray-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								id="averageCostHeader">
								Average cost
								<span className="sort-icon">&darr;</span>
							</th>
							<th
								className="cursor-pointer border-gray-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								id="returnHeader">
								Total return
								<span className="sort-icon">&darr;</span>
							</th>
							<th
								className="cursor-pointer border-gray-300 px-6 py-4 text-gray-500 hover:border-b hover:text-black"
								id="equityHeader">
								Equity
								<span className="sort-icon">&darr;</span>
							</th>
						</tr>
					</thead>
					<tbody>
						<tr className="border-b border-gray-300 hover:bg-gray-100">
							<td className="whitespace-nowrap px-6 py-4 font-bold">Visa</td>
							<td className="whitespace-nowrap px-6 py-4">V</td>
							<td className="whitespace-nowrap px-6 py-4">10</td>
							<td className="whitespace-nowrap px-6 py-4">$250</td>
							<td className="whitespace-nowrap px-6 py-4">$200</td>
							<td className="whitespace-nowrap px-6 py-4">$500</td>
							<td className="whitespace-nowrap px-6 py-4">$2,500</td>
						</tr>
						<tr className="border-b border-gray-300 hover:bg-gray-100">
							<td className="whitespace-nowrap px-6 py-4 font-bold">Apple</td>
							<td className="whitespace-nowrap px-6 py-4">AAPL</td>
							<td className="whitespace-nowrap px-6 py-4">10</td>
							<td className="whitespace-nowrap px-6 py-4">$150</td>
							<td className="whitespace-nowrap px-6 py-4">$100</td>
							<td className="whitespace-nowrap px-6 py-4">$500</td>
							<td className="whitespace-nowrap px-6 py-4">$1,500</td>
						</tr>
						<tr className="border-b border-gray-300 hover:bg-gray-100">
							<td className="whitespace-nowrap px-6 py-4 font-bold">Amazon</td>
							<td className="whitespace-nowrap px-6 py-4">AMZN</td>
							<td className="whitespace-nowrap px-6 py-4">150</td>
							<td className="whitespace-nowrap px-6 py-4">$100</td>
							<td className="whitespace-nowrap px-6 py-4">$150</td>
							<td className="whitespace-nowrap px-6 py-4">$-50</td>
							<td className="whitespace-nowrap px-6 py-4">$100</td>
						</tr>
					</tbody>
				</table>
			</div>
			{/* Donut Chart */}
			<div className="w-1/2 chart-container">
				<div className="bg-white border border-gray-300 rounded-lg shadow p-4">
					<canvas
						id="myDoughnutChart"
						width="200"
						height="200"></canvas>
					<div className="center-text">
						<div className="text-s font-semibold">Stocks and Options</div>
						<div className="text-sm">Amount</div>
						<div className="text-xs font-bold">75%</div>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Profile;
