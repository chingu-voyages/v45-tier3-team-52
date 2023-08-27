import React, { useState } from "react";
import { useNavigate } from "react-router";

const textInputStyle = "text-xs";
const inputStyle =
	"border-solid border-gray-300 border w-full mt-2 py-1 px-2 rounded text-black";

const AuthForm = props => {
	const { formType } = props;
	const navigate = useNavigate();
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [firstName, setfirstName] = useState("");
	const [lastName, setLastName] = useState("");

	const registerName = (
		<>
			<div>
				<label htmlFor="first-name">
					<div className={textInputStyle}>First Name</div>
				</label>
				<input
					id="first-name"
					type="text"
					value={firstName}
					onChange={e => setfirstName(e.target.value)}
					required
					className={inputStyle}
				/>
			</div>
			<div>
				<label htmlFor="last-name">
					<div className={textInputStyle}>Last Name</div>
				</label>
				<input
					id="last-name"
					type="text"
					value={lastName}
					onChange={e => setLastName(e.target.value)}
					required
					className={inputStyle}
				/>
			</div>
		</>
	);

	const sessionDisclaimer = (
		<p className="text-xs">
			This clone is for educational purposes only. Please do not put any
			sensitive information.
		</p>
	);

	return (
		<div className="h-full flex items-center justify-center bg-black text-white">
			<div className="flex flex-col gap-5 mx-10 w-full">
				<div className="text-xl">
					{formType === "Register" ? "Sign up" : "Log in"} to Robinhood
				</div>
				<form className="flex flex-col gap-5">
					{formType === "Register" && registerName}
					<div>
						<label htmlFor="email-address">
							<div className={textInputStyle}>Email address</div>
						</label>
						<input
							id="email-address"
							type="text"
							value={email}
							onChange={e => setEmail(e.target.value)}
							required
							className={inputStyle}
						/>
					</div>
					<div>
						<label htmlFor="password">
							<div className={textInputStyle}>Password</div>
						</label>
						<input
							id="password"
							type="password"
							value={password}
							onChange={e => setPassword(e.target.value)}
							required
							className={inputStyle}
						/>
					</div>
				</form>
				<button className="my-5 border-solid border-black-500 border w-full h-10 rounded-full bg-black text-white hover:cursor-pointer hover:bg-gray-300 hover:border-gray-300">
					<div className="text-xs">
						{formType === "Register" ? "Register" : "Log in"}
					</div>
				</button>
				{/* {formType === "Log in" && } */}
				<div className="flex gap-1 text-xs">
					<div>
						{formType === "Register" ? "Have an account?" : "Not on Robinhood?"}
					</div>
					<button
						className="hover:cursor-pointer"
						onClick={() =>
							formType === "Register"
								? navigate("/login")
								: navigate("/register")
						}>
						<div className="font-bold border-b-2 border-white">
							{formType === "Register" ? "Log in" : "Create an account"}
						</div>
					</button>
				</div>
				{formType === "Register" && sessionDisclaimer}
			</div>
		</div>
	);
};

export default AuthForm;
