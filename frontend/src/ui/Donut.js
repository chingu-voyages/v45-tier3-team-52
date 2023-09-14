const dataTop = {
	labels: ["Red", "Blue", "Yellow", "Green", "Purple"],
	datasets: [
		{
			data: [12, 19, 3, 5, 2],
			backgroundColor: [
				"rgb(49, 200, 5)",
				"rgb(49, 200, 5)",
				"rgb(49, 200, 5)",
				"rgb(49, 200, 5)",
				"rgb(49, 200, 5)",
			],
			borderColor: ["white", "white", "white", "white", "white"],
			borderWidth: 2,
		},
	],
};

const configTop = {
	type: "doughnut",
	data: dataTop,
	options: {
		responsive: false, // Disable responsiveness
		maintainAspectRatio: false, // Disable aspect ratio
	},
};

// Initialize and render the top chart
const ctxTop = document.getElementById("myDoughnutChartTop").getContext("2d");
new Chart(ctxTop, configTop);
