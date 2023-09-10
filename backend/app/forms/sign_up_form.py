from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(
        min=4, max=40), user_exists])
    password = StringField('Password', validators=[DataRequired(), Length(
        min=9, max=40)])
    first_name = StringField('First Name', validators=[DataRequired(), Length(
        min=4, max=40)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(
        min=4, max=40)])
