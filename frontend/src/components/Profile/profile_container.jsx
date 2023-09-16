import React from "react";
import { connect } from "react-redux";
import Profile from "./profile";

const mapStateToProps = state => {
	// const {
	// 	session,
	// 	entities: { users },
	// } = state;

	return {
		// currentUser: users[session.id],
	};
};

const mapDispatchToProps = state => {
	return {};
};

export default connect(mapStateToProps, mapDispatchToProps)(Profile);
