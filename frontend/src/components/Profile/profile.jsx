// import React from "react";
import React, { useState } from "react";

const Profile = () => {
	const [modal, setModal] = useState(false);
	return (
		<body className="font-times text-base ml-4 mr-12">
			{modal && <div onClick={() => setModal(false)}>Modal</div>}
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
