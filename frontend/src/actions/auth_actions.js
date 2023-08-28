import * as AuthApiUtil from "../util/auth_api_util";

export const LOGIN_CURRENT_USER = "LOGIN_CURRENT_USER";
export const RECEIVE_SESSION_ERRORS = "RECEIVE_SESSION_ERRORS";
export const LOGOUT_CURRENT_USER = "LOGOUT_CURRENT_USER";
export const CLEAR_ERRORS = "CLEAR_ERRORS";

export const loginCurrentUser = currentUser => ({
	type: LOGIN_CURRENT_USER,
	currentUser,
});

export const logoutCurrentUser = () => ({
	type: LOGOUT_CURRENT_USER,
});

export const receiveErrors = errors => ({
	type: RECEIVE_SESSION_ERRORS,
	errors,
});

export const clearErrors = () => ({
	type: CLEAR_ERRORS,
});

export const register = user => async dispatch => {
	try {
		const res = await AuthApiUtil.register(user);
		const newUser = res.data;
		dispatch(loginCurrentUser(newUser));
	} catch (err) {
		const error = err.response.data;
		dispatch(receiveErrors(error));
	}
};

export const login = user => async dispatch => {
	try {
		const res = await AuthApiUtil.login(user);
		const loggedInUser = res.data;
		dispatch(loginCurrentUser(loggedInUser));
	} catch (err) {
		const error = err.response.data;
		dispatch(receiveErrors(error));
	}
};

export const logout = () => async dispatch => {
	try {
		await AuthApiUtil.logout();
		dispatch(logoutCurrentUser());
	} catch (err) {
		console.error("Error logging out", err);
	}
};
