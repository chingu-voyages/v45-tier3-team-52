import React, { useEffect, useState } from "react";
import Highcharts from "highcharts/highstock";
import HighchartsReact from "highcharts-react-official";
import axios from "axios";
import { stockChartOptions } from "../../util/stockChart_util";

// ----- remove "Zoom" text next to button
Highcharts.setOptions({
	lang: {
		rangeSelectorZoom: "",
	},
	colors: ["#00C805"],
});

const StockChart = () => {
	const [loading, setLoading] = useState(true);
	const [options, setOptions] = useState(stockChartOptions);

	const fetchData = async () => {
		try {
			// TODO: change to our API
			const response = await axios.get(
				"https://demo-live-data.highcharts.com/aapl-ohlc.json"
			);

			const newOptions = options;
			newOptions.series[0].data = response.data;
			setOptions(newOptions);
			setLoading(false);
		} catch (error) {
			console.log("error:", error);
			setLoading(false);
		}
	};

	useEffect(() => {
		fetchData();
	}, []);

	return (
		<div className="flex justify-center items-center h-full">
			{!loading && (
				<div className="border-2 border-red-500 w-1/2">
					<HighchartsReact
						highcharts={Highcharts}
						constructorType={"stockChart"}
						options={options}
					/>
				</div>
			)}
		</div>
	);
};

export default StockChart;
