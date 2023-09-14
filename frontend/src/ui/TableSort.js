document.addEventListener("DOMContentLoaded", function () {
	const header1 = document.getElementById("header1");
	const sortIcon = header1.querySelector(".sort-icon");
	let ascending = true;

	header1.addEventListener("click", () => {
		header1.classList.toggle("text-green-500");

		if (ascending) {
			sortIcon.textContent = "↓";
		} else {
			sortIcon.textContent = "↑";
		}

		sortTable(0, ascending);
		ascending = !ascending;
	});

	// Function to sort the table
	function sortTable(column, ascending) {
		const table = document.querySelector("table");
		const tbody = table.querySelector("tbody");
		const rows = Array.from(tbody.querySelectorAll("tr"));

		rows.sort((rowA, rowB) => {
			const cellA = rowA.querySelectorAll("td")[column].textContent.trim();
			const cellB = rowB.querySelectorAll("td")[column].textContent.trim();

			if (ascending) {
				return cellA.localeCompare(cellB);
			} else {
				return cellB.localeCompare(cellA);
			}
		});

		// Clear the table body and append sorted rows
		while (tbody.firstChild) {
			tbody.removeChild(tbody.firstChild);
		}

		rows.forEach(row => tbody.appendChild(row));
	}
});
