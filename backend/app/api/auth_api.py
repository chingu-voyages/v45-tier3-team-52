from flask import Blueprint, redirect, url_for, request
from flask_login import login_user, logout_user
from app.models import User, db
from .forms import LoginForm, RegisterForm


auth_routes = Blueprint("auth", __name__)


@auth_routes.route("/login", methods=['POST'])
def login():
    form = LoginForm()
    print('----->', form.data)
    print('------request',request.json)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        print('---......>>>','what is it')
        user = User.query.filter(User.email == form.data['email']).first()
        print('------>',user)
        login_user(user)
        return user.to_dict()
    return {'error': 'failed to log in'}, 401


@auth_routes.route("/register", methods=['POST'])
def register():
    form = RegisterForm()
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
        login_user(new_user)
        return new_user.to_dict()
    return {'error': 'registration failed'}, 401


@auth_routes.route("/logout")
def logout():
    logout_user()
    return {"message": "logout works"}
