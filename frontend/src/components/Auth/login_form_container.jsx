import React from "react";
import { connect } from "react-redux";
import { login, clearErrors } from "../../actions/session_actions";
import { showModal, hideModal } from "../../actions/modal_actions";
import SessionForm from "./session_form";
import { withRouter } from "react-router-dom";

const mSTP = props => {
	const { errors } = props;

	return {
		errors: errors.session,
		formType: "Sign in",
	};
};

const mDTP = dispatch => {
	return {
		processForm: user => dispatch(login(user)),
		// other form is another site
		// otherForm: (
		// 	<span
		// 		className="other-form"
		// 		onClick={() => dispatch(showModal("Register"))}>
		// 		register
		// 	</span>
		// ),
		hideModal: () => dispatch(hideModal()),
		clearErrors: () => dispatch(clearErrors()),
	};
};

export default withRouter(connect(mSTP, mDTP)(SessionForm));
