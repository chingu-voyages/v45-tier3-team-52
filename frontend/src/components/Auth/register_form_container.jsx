// switch session => auth, signup => register

import React from "react";
import { connect } from "react-redux";
import { signup, clearErrors } from "../../actions/session_actions";
import SessionForm from "./session_form";
import { showModal, hideModal } from "../../actions/modal_actions";
import { withRouter } from "react-router-dom";

const mSTP = props => {
	const { errors } = props;
	return {
		errors: errors.session,
		formType: "Register",
	};
};

const mDTP = dispatch => ({
	processForm: user => dispatch(signup(user)),
	// otherForm: (
	// 	<span
	// 		className="other-form"
	// 		onClick={() => dispatch(showModal("Sign in"))}>
	// 		sign in
	// 	</span>
	// ),
	// hideModal: () => dispatch(hideModal()),
	clearErrors: () => dispatch(clearErrors()),
});

export default withRouter(connect(mSTP, mDTP)(SessionForm));
