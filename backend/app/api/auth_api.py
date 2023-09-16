from flask import Blueprint, request
from flask_login import login_user, logout_user, current_user
from app.models import User, db, UserPortfolio


auth_routes = Blueprint("auth", __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

############ * Authentication #######################################


@auth_routes.route('/')
def authentication():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


############ * Login #######################################


@auth_routes.route("/login", methods=['POST'])
def login():
    req_data = request.json
    user = User.query.filter(User.email == req_data['email']).first()
    if not user:
        return {'errors': "user can not be found"}, 401
    if not user.check_password(req_data['password']):
        raise {'errors': 'Password was incorrect.'}
    login_user(user)

    return user.to_dict()

############ * Register #######################################


@auth_routes.route("/register", methods=['POST'])
def register():
    req_data = request.json
    user = User.query.filter(User.email == req_data['email']).first()
    if user:
        return {'errors': "user exists"}, 401
    if not user:
        new_user = User(
            first_name=req_data['first_name'],
            last_name=req_data['last_name'],
            email=req_data['email'],
            password=req_data['password'],
        )
        db.session.add(new_user)
        db.session.commit()
        new_portfolio_user = UserPortfolio(
            user_id=new_user.id
        )
        db.session.add(new_portfolio_user)
        db.session.commit()
        login_user(new_user)
        return new_user.to_dict()
    else:
        return {'error': 'Registration failed'}, 401


############ * Logout #######################################

@auth_routes.route("/logout")
def logout():
    logout_user()
    return {"message": "User was logged out"}
