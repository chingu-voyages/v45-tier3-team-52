import React from "react";
import { connect } from "react-redux";
import { login, clearErrors } from "../../actions/auth_actions";
import AuthForm from "./auth_form";

const mapStateToProps = state => {
	const { errors } = state;

	return {
		errors: errors.session,
		formType: "Sign in",
	};
};

const mapDispatchToProps = dispatch => {
	return {
		processForm: user => dispatch(login(user)),
		// clearErrors: () => dispatch(clearErrors()),
	};
};

export default connect(mapStateToProps, mapDispatchToProps)(AuthForm);
