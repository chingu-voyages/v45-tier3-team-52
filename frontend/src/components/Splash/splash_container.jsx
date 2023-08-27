import React from "react";
import { connect } from "react-redux";
import Splash from "./splash";
import { useNavigate } from "react-router-dom";

const mapStateToProps = state => {
	const {
		session,
		entities: { users },
	} = state;

	return {
		// currentUser: users[session.id],
	};
};

const mapDispatchToProps = state => {
	return {};
};

export default connect(mapStateToProps, mapDispatchToProps)(Splash);
