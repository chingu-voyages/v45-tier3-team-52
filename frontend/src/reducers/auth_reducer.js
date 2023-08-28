import {
	LOGIN_CURRENT_USER,
	LOGOUT_CURRENT_USER,
} from "../actions/auth_actions";

const _nullSession = {
	id: null,
};

const authReducer = (state = _nullSession, action) => {
	Object.freeze(state);
	let nextState = Object.assign({}, state);
	switch (action.type) {
		case LOGIN_CURRENT_USER:
			return Object.assign({}, { id: action.currentUser.id });
		case LOGOUT_CURRENT_USER:
			return _nullSession;
		default:
			return state;
	}
};

export default authReducer;
