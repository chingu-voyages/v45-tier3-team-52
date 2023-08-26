import React from "react";
import { connect } from "react-redux";
import Splash from "./splash";
import { useNavigate } from "react-router-dom";

const SplashContainer = ({ currentUser }) => {
	const navigate = useNavigate();

	return (
		<Splash
			currentUser={currentUser}
			navigate={navigate}
		/>
	);
};

const mapStateToProps = state => {
	const {
		session,
		entities: { users },
	} = state;

	return {
		// currentUser: users[session.id],
	};
};

export default connect(mapStateToProps)(SplashContainer);
