from flask import Blueprint, request
from flask_login import login_user, logout_user
from app.models import User, db, UserPortfolio
from app.forms import LoginForm, SignUpForm


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


@auth_routes.route("/login", methods=['POST'])
def login():
    form = LoginForm()
    print("userdata ===> ", type(form.data['email']))
    form['csrf_token'].data = request.cookies['csrf_token']
    print("Request Form Data ===>", request.form)
    print("Request Cookies ===>", request.cookies)

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.data['email']).first()
        print("queried user ===>", user)
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route("/register", methods=['POST'])
def register():
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_user = User(
            first_name=form.data['first_name'],
            last_name=form.data['last_name'],
            email=form.data['email'],
            password=form.data['password'],
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
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route("/logout")
def logout():
    logout_user()
    return {"message": "User was logged out"}
