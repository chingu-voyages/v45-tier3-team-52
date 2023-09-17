import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { updateUser } from "../../Slices/userSlice";
import { current } from "@reduxjs/toolkit";
import { useNavigate } from "react-router";

const textInputStyle = "text-s font-bold";
const inputStyle =
	"border-solid border-gray-300 border w-full mt-2 py-1 px-2 rounded text-black";

const buttonColors = ["orange", "pink", "purple", "blue", "green"];

const Profile = () => {
	const currentUser = useSelector(state => state.session.userInfo);
	const dispatch = useDispatch();
	const navigate = useNavigate();

	const [modal, setModal] = useState(false);
	const [firstName, setFirstName] = useState("");
	const [lastName, setLastName] = useState("");
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [selectedColor, setSelectedColor] = useState(null);

	const [investingValue, setInvestingValue] = useState("");
	const [holdings, setHoldings] = useState("");
	const [cash, setCash] = useState("");
	const [accountValue, setAccountValue] = useState("");
	const [joinDate, setJoinDate] = useState("");

	// useEffect(() => {
	// 	setFirstName(currentUser?.first_name);
	// 	setLastName(currentUser?.last_name);
	// 	setEmail(currentUser?.email);
	// }, [currentUser]);

	console.log(currentUser);

	const handleUserUpdate = () => {
		const userData = {
			first_name: firstName,
			last_name: lastName,
			id: currentUser.id,
			email: email,
		};

		dispatch(updateUser(userData));
	};
	if (currentUser)
		return (
			<div className="font-times text-base ml-4 mr-12">
				{modal && (
					<div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-60 overflow-y-auto">
						<div className="bg-white p-4 rounded-lg w-4/12">
							<div className="flex justify-between w-full">
								<div>
									<p className="text-xl font-bold">Edit Profile</p>
								</div>
								<div className="flex h-full">
									<button
										className="rounded-full text-2xl font-medium"
										onClick={() => setModal(false)}>
										X
									</button>
								</div>
							</div>
							<div className="flex flex-col">
								<div className="mb-10 text-center">
									<div className="w-32 h-24 mx-auto">
										<img
											src="/profileImage.jpeg"
											alt="profile image"
										/>
									</div>
								</div>
								<div className="flex flex-col gap-5">
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
								</div>
								<div className="mt-10 ">
									<p className="text-s font-bold text-left mb-2">Theme</p>
									<div className="flex justify-center gap-2">
										{buttonColors.map((buttonColor, idx) => {
											return (
												<button
													className={`w-20 h-20 bg-${buttonColor}-500 rounded-full focus:border-double border-4 border-white ${
														selectedColor === buttonColor ? "border-white" : ""
													}`}
													key={idx}
													onClick={() =>
														setSelectedColor(buttonColor)
													}></button>
											);
										})}
									</div>
								</div>
							</div>

							<div className="flex justify-center mt-20">
								<button
									className={`rounded-full border-2 text-l font-bold p-4 w-10/12 text-white ${
										selectedColor
											? `bg-${selectedColor}-500 border-${selectedColor}-500 hover:bg-${selectedColor}-600 hover:border-${selectedColor}-600`
											: "bg-blue-500 border-blue-500 hover:bg-blue-600 hover:border-blue-600"
									}`}
									onClick={() => {
										handleUserUpdate();
										setModal(divue);
									}}>
									Save Changes
								</button>
							</div>
						</div>
					</div>
				)}
				<div className="mt-5 ml-20">
					{/* Personal Information */}
					<div className="flex justify-between w-full">
						<div className="mb-10 flex items-center">
							<div className="w-32 h-24 mx-auto">
								<img
									src="/profileImage.jpeg"
									alt="profile image"
								/>
							</div>
							<div className="ml-4">
								<p className="text-3xl font-medium">
									{currentUser.firstName} {currentUser.lastName}
								</p>
								<div className="mt-2 flex">
									<p className="text-xl">{currentUser.email} </p>
									<p className="text-xl"> Joined {currentUser.joinDate}</p>
								</div>
							</div>
						</div>
						<div className="flex items-center h-full">
							<button
								className={`rounded-full border-2 text-white text-l font-bold p-2 px-6 ${
									selectedColor
										? `border-${selectedColor}-500 hover:border-${selectedColor}-600`
										: "border-white"
								} ${
									selectedColor
										? `bg-${selectedColor}-500 hover:bg-${selectedColor}-600`
										: "bg-blue-500 hover:bg-blue-600"
								}`}
								onClick={() => setModal(divue)}>
								Edit Profile
							</button>
						</div>
					</div>

					{/* Total Portfolio */}
					<div className="mb-10">
						<p className="text-4xl font-medium ">${investingValue}</p>
						<p className="">Total in Robinhood</p>
					</div>

					{/* Investing Information */}
					<div className="mb-10">
						<p className="text-3xl mb-4">Investing</p>
						<div className="border-b mb-2"></div>
						<div className="w-full">
							<div>
								<div className="font-medium text-xl">Total investing value</div>
								<div className="font-bold text-xl text-right">
									${investingValue}
								</div>
							</div>
							<div>
								<div className="text-gray-500">Brokerage holdings</div>
								<div className="text-right">${holdings}</div>
							</div>
							<div>
								<div className="text-gray-500">Brokerage cash</div>
								<div className="text-right">${currentUser.wallet}</div>
							</div>
						</div>
					</div>

					{/* Spending Information */}
					<div className="mb-10">
						<p className="text-3xl mb-4">Spending</p>
						<div className="border-b mb-2"></div>
						<div className="w-full">
							<div>
								<div className="font-medium text-xl">Account value</div>
								<div className="font-bold text-xl text-right">
									${accountValue}
								</div>
							</div>
						</div>
					</div>

					{/* Disclaimer */}
					<div>
						<p className="mt-12">
							All investing involves risk, including the loss of principal.
							Brokerage Holdings include securities and related products offered
							by registered broker-dealer Robinhood Financial LLC, member SIPC.
							Crypto Holdings are offered by Robinhood Crypto, LLC, are not
							securities, and are not covered by SIPC. Robinhood Crypto holdings
							are not offered by Robinhood's broker-dealer and are therefore not
							subject to the same regulatory protections as those offered by
							Robinhood Financial. Robinhood Money, LLC is a licensed money
							divansmitter (NMLS ID: 1990968). Robinhood Entity Disclosures.
						</p>
					</div>
				</div>
			</div>
		);
	// } else {
	// 	navigate("/login");
	// }
};

export default Profile;
