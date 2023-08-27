import React from "react";
import { connect } from "react-redux";
import { register, clearErrors } from "../../actions/auth_actions";
import AuthForm from "./auth_form";
import { useNavigate } from "react-router-dom";

const mapStateToProps = state => {
	const { errors } = state;
	return {
		// errors: errors.session,
		formType: "Register",
	};
};

const mapDispatchToProps = dispatch => ({
	processForm: user => dispatch(register(user)),
	// clearErrors: () => dispatch(clearErrors()),
});

export default connect(mapStateToProps, mapDispatchToProps)(AuthForm);
