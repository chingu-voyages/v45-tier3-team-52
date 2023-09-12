import { useDispatch, useSelector } from "react-redux";
import { loginUser } from "../Auth/authSlice";

const Login = () => {
	const dispatch = useDispatch();
	const demoLogin = async () => {
		const userCredentials = {
			email: "cantuk0@harvard.edu",
			password: "zF8*wiaMl",
		};
		await dispatch(loginUser(userCredentials));
	};

	return (
		<div>
			<button
				onClick={() => {
					demoLogin();
				}}
				className="cursor-pointer p-[2px] text-sm text-blue-700 font-bold md:text-sm whitespace-nowrap rounded-lg focus:outline-none focus:ring-2 bg-gradient-to-b from-slate-100 to-slate-200 focus:ring-yellow-500 active:from-slate-200 px-3 py-2 border-[1px] border-ninja_green-dark">
				Demo Login
			</button>
		</div>
	);
};

export default Login;
