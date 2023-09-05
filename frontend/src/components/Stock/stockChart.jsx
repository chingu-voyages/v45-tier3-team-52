import React from "react";
import Highcharts from "highcharts/highstock";
import HighchartsReact from "highcharts-react-official";

const options = {
	title: {
		text: "",
	},
	series: [
		{
			data: [1, 2, 3],
		},
	],
};

const stockOptions = {
	yAxis: [
		{
			height: "75%",
			labels: {
				align: "right",
				x: -3,
			},
			title: {
				text: "AAPL",
			},
		},
	],
};

const StockChart = () => {
	return (
		<div className="flex justify-center items-center h-full">
			<div className="w-1/2">
				<HighchartsReact
					highcharts={Highcharts}
					constructorType={"stockChart"}
					options={options}
				/>
			</div>
		</div>
	);
};

export default StockChart;
