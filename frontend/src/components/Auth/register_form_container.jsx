// switch session => auth, signup => register

import React from "react";
import { connect } from "react-redux";
import { signup, clearErrors } from "../../actions/auth_actions";
import AuthForm from "./auth_form";
import { useNavigate } from "react-router-dom";

const mapStateToProps = state => {
	const { errors } = props;
	return {
		errors: errors.session,
		formType: "Register",
	};
};

const mapDispatchToProps = dispatch => ({
	processForm: user => dispatch(signup(user)),
	// clearErrors: () => dispatch(clearErrors()),
});

export default connect(mapStateToProps, mapDispatchToProps)(AuthForm);
