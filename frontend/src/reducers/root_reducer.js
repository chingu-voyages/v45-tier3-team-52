import { combineReducers } from "redux";
import entitiesReducer from "./entities_reducer";
import authReducer from "./auth_reducer";
import errorsReducer from "./errors_reducer";
import uiReducer from "./ui_reducer";

const rootReducer = combineReducers({
	// entities: entitiesReducer,
	auth: authReducer,
	// errors: errorsReducer,
	// ui: uiReducer,
});

export default rootReducer;
