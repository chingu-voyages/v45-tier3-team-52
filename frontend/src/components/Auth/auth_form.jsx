import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router";
// import robinhood from "../../assets/robinhoodBG.jpeg";
import { loginUser } from "../Slices/authSlice";

const textInputStyle = "text-xs";
const inputStyle =
	"border-solid border-gray-300 border w-full mt-2 py-1 px-2 rounded text-black";

const authDesktopStyle = "lg:flex";

const AuthForm = props => {
	const { formType } = props;
	const navigate = useNavigate();
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [firstName, setFirstName] = useState("");
	const [lastName, setLastName] = useState("");

	const dispatch = useDispatch();
	const demoLogin = async () => {
		const demoCredentials = {
			email: "cantuk0@harvard.edu",
			password: "zF8*wiaMl",
		};
		await dispatch(loginUser(demoCredentials));
	};

	const handleLogin = async () => {
		const userCredentials = {
			email,
			password,
		};
		await dispatch(loginUser(userCredentials));
	};

	const registerName = (
		<div className="flex flex-col gap-5 md:flex-row lg:flex-col">
			<div className="w-full">
				<label htmlFor="first-name">
					<div className={textInputStyle}>First Name</div>
				</label>
				<input
					id="first-name"
					type="text"
					value={firstName}
					onChange={e => setFirstName(e.target.value)}
					required
					className={inputStyle}
				/>
			</div>
			<div className="w-full">
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
		</div>
	);

	const sessionDisclaimer = (
		<p className="text-xs">
			This clone is for educational purposes only. Please do not put any
			sensitive information.
		</p>
	);

	const desktopDisplay =
		formType === "Register" ? (
			<div className="hidden lg:flex h-full w-1/2 items-center justify-center px-16 bg-[#82c8d2]">
				<div className="flex flex-col h-5/6 gap-24">
					<div className="text-2xl text-gray-700">Robinhood</div>
					<div className="flex flex-col gap-12">
						<h1 className="text-7xl leading-[5rem]">Create your login</h1>
						<p>
							We&apos;ll need your name, email address and a unique password.
							You&apos;ll use this login to access Robinhood next time.
						</p>
					</div>
				</div>
			</div>
		) : (
			<div className="sm:hidden lg:block lg:w-1/2 lg:bg-[#82c8d2] bg-[url('/robinhoodBG.jpeg')] bg-cover"></div>
		);

	const authFormDisplay = (
		<div className="h-full flex items-center justify-center lg:w-1/2">
			<div className="flex flex-col gap-5 mx-10 w-full md:mx-20 lg:mx-10">
				<div className="text-xl">
					{formType === "Register"
						? "Register for a Robhinhood account"
						: "Log in"}
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
				<button
					className="my-5 border-solid border-black-500 border w-full h-10 rounded-full bg-black text-white hover:cursor-pointer hover:bg-gray-300 hover:border-gray-300"
					onClick={handleLogin}>
					<div className="text-xs">
						{formType === "Register" ? "Register" : "Log in"}
					</div>
				</button>
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
						<div className="font-bold border-b-2 border-black">
							{formType === "Register" ? "Log in" : "Create an account"}
						</div>
					</button>
				</div>
				{formType === "Register" && sessionDisclaimer}
			</div>
		</div>
	);

	return (
		<div className={`h-full w-full ${authDesktopStyle}`}>
			{desktopDisplay}
			{authFormDisplay}
		</div>
	);
};

export default AuthForm;
