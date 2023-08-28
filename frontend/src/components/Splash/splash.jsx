import React from "react";
import { useNavigate } from "react-router";
// import splashBG from "/splashBG.jpeg";

const Splash = () => {
	const navigate = useNavigate();
	return (
		<div className="text-[#FFC757] bg-black flex flex-col lg:h-full">
			<div className="py-4 px-6 flex justify-between border-b border-[#FFC757]">
				<div className="text-3xl">Robinhood</div>
				<button
					onClick={() => navigate("/register")}
					className="rounded-full bg-[#FFC757] text-black w-20 text-xs font-semibold border-[#FFC757] border hover:bg-black hover:text-[#FFC757] ">
					<div>Sign up</div>
				</button>
			</div>
			<div className="px-6 md:px-24 text-sm md:text-lg flex items-center justify-center bg-black">
				<div className=" flex flex-col gap-5 py-10">
					<div className="bg-[url('/splashMobileBG.jpeg')] lg:bg-[url('/splashDesktopBG.jpeg')] bg-auto lg:bg-contain bg-center h-96 bg-no-repeat"></div>

					<p className="text-white font-light leading-[2rem] text-center ">
						Tomorrow starts today with our highest rate ever on uninvested cash,
						FDIC-insured up to $2M at partner banks.* First 30 days free, then
						just $5/month.
					</p>
					<div className="flex justify-center">
						<button
							onClick={() => navigate("/register")}
							className="rounded-full bg-[#FFC757] w-fit text-black font-bold border-[#FFC757] border hover:bg-black hover:text-[#FFC757] py-4 px-8 flex">
							Earn 4.9% APY
						</button>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Splash;
