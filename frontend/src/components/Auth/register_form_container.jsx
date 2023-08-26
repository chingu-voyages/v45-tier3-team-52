// switch session => auth, signup => register

import React from "react";
import { connect } from "react-redux";
import { signup, clearErrors } from "../../actions/auth_actions";
// import { showModal, hideModal } from "../../actions/modal_actions";
import AuthForm from "./auth_form";
import { useNavigate } from "react-router-dom"; // Import useNavigate

const RegisterFormContainer = props => {
	const navigate = useNavigate();
	const { formType } = props;
	return <AuthForm formType={formType} />;
};

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

export default connect(mapStateToProps, mapDispatchToProps)(LoginFormContainer);
