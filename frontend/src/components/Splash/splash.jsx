import React from "react";
import { useNavigate } from "react-router";

const Splash = () => {
	const navigate = useNavigate();
	return (
		<div>
			<div className="p-2 flex justify-between">
				<div>Robinhood</div>
				<button onClick={() => navigate("/register")}>
					<div>Sign up</div>
				</button>
			</div>
			<div></div>
		</div>
	);
};

export default Splash;
