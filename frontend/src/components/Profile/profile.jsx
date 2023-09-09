// import React from "react";
import React, { useState } from "react";
const textInputStyle = "text-xs";
const inputStyle =
	"border-solid border-gray-300 border w-full mt-2 py-1 px-2 rounded text-black";

const Profile = () => {
	const [modal, setModal] = useState(false);
	const [firstName, setfirstName] = useState("");
	const [lastName, setLastName] = useState("");
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	return (
		<body className="font-times text-base ml-4 mr-12">
			{modal && (
				<div onClick={() => setModal(false)}>
					<section className="flex justify-between w-full">
						<div className="">
							<p className="text-xl font-bold">Edit Profile</p>
						</div>
						<div className="flex h-full">
							<button
								className="rounded-full  text-2xl font-medium"
								onClick={() => setModal(false)}>
								X
							</button>
						</div>
					</section>
					<div className="flex justify-center mt-10">
						<img
							src="pic_trulli.jpg"
							alt="profile image"
						/>
					</div>
					<div>
						<div className="flex flex-col gap-5 md:flex-row lg:flex-col">
							<div className="w-full">
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
					</div>
				</div>
			)}
			<div className="mt-5 ml-20">
				{/* Personal Information */}
				<section className="flex justify-between w-full">
					<div className="mb-10">
						<p className="text-3xl mt-2 ml-12 font-medium">Jonathan s</p>
						<p className="mt-2 ml-12 text-xl">@jsiu1248 . Joined 2015</p>
					</div>
					<div className="flex items-center h-full">
						<button
							className="rounded-full border-2 text-l font-bold p-2 px-6 border-black"
							onClick={() => setModal(true)}>
							Edit Profile
						</button>
					</div>
				</section>

				{/* Total Portfolio */}
				<div className="mb-10">
					<p className="text-4xl font-medium ">$Amount</p>
					<p className="">Total in Robinhood</p>
				</div>

				{/* Investing Information */}
				<div className="mb-10">
					<p className="text-3xl mb-4">Investing</p>
					<div className="border-b mb-2"></div>
					<table className="w-full">
						<tr>
							<td className="p-2 font-medium text-xl">Total investing value</td>
							<td className="p-2 font-bold text-xl text-right">$Amount</td>
						</tr>
						<tr>
							<td className="p-2 text-gray-500">Brokerage holdings</td>
							<td className="p-2 text-right">$Amount</td>
						</tr>
						<tr>
							<td className="p-2 text-gray-500">Brokerage cash</td>
							<td className="p-2 text-right">$Amount</td>
						</tr>
					</table>
				</div>

				{/* Spending Information */}
				<div className="mb-10">
					<p className="text-3xl mb-4">Spending</p>
					<div className="border-b mb-2"></div>
					<table className="w-full">
						<tr>
							<td className="p-2 font-medium text-xl">Account value</td>
							<td className="p-2 font-bold text-xl text-right">$0.00</td>
						</tr>
					</table>
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
						transmitter (NMLS ID: 1990968). Robinhood Entity Disclosures.
					</p>
				</div>
			</div>
		</body>
	);
};

export default Profile;
