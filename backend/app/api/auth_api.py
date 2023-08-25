from flask import Blueprint, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, db 
from .forms import LoginForm, RegisterForm

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # if bcrypt.check_password_hash(user.password, form.password.data)
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        # return user.to_dict()
        return {"message": "login works"}


@auth_routes.route("/register", methods=['POST'])
def register():
    form = RegisterForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        print("on validate")
        new_user = User(
            first_name=form.data['first_name'],
            last_name=form.data['last_name'],
            email=form.data['email'],
            password=form.data['password'],
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        # return new_user.to_dict()
        return {"message": "register works"}
    else:
        print("not validate")
    
@auth_routes.route("/logout")
def logout():
    logout_user()
    # redirect(url_for("login"))
    return {"message": "logout works"}
    


