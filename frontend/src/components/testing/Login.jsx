import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { loginUser } from "../Auth/authSlice";
import { useNavigate } from "react-router-dom";

const Login = () => {
	// states
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	// redux state

	const test = useSelector(state => state.auth);
	const navigate = useNavigate();
	const dispatch = useDispatch();
	// useEffect(() => {
	// 	async () => {};
	// });

	const handleLoginEvent = e => {
		e.preventDefault();
		let userCredentials = {
			email,
			password,
		};
		dispatch(loginUser(userCredentials)).then(result => {
			if (result.payload) {
				setEmail("");
				setPassword("");
				navigate("/");
			}
		});
	};

	return (
		<form onSubmit={handleLoginEvent}>
			<label>Email</label>
			<input
				type="email"
				required
				className=""
				value={email}
				onChange={e => setEmail(e.target.value)}
			/>
			<br />
			<label>Password</label>
			<input
				type="password"
				required
				className=""
				value={password}
				onChange={e => setPassword(e.target.value)}
			/>
			<br />
			<button
				type="submit"
				className="">
				{/* {loading ? "Loading..." : "Login"} */}
				Login
			</button>
			{/* {error && (
				<div
					className=""
					role="alert">
					{error}
				</div>
			)} */}
		</form>
	);
};

export default Login;
