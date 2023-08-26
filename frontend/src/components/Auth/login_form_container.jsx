import React from "react";
import { connect } from "react-redux";
import { login, clearErrors } from "../../actions/auth_actions";
import AuthForm from "./auth_form";
import { useNavigate } from "react-router-dom";

const LoginFormContainer = props => {
	const navigate = useNavigate();

	const {
		errors,
		processForm,
		// hideModal,
		clearErrors,
		// otherForm,
		formType,
	} = props;

	// Your component logic here, if needed

	return (
		<AuthForm
			// errors={errors}
			// processForm={processForm}
			clearErrors={clearErrors}
			navigate={navigate}
			formType={formType}
		/>
	);
};

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

export default connect(mapStateToProps, mapDispatchToProps)(LoginFormContainer);
