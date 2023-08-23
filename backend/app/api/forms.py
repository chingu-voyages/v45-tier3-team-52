from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError



class RegisterForm(FlaskForm):
    first_name = StringField(validators=[DataRequired(), Length(
        min=4, max=40)])
    
    last_name = StringField(validators=[DataRequired(), Length(
        min=4, max=40)])
    
    email = StringField(validators=[DataRequired(), Length(
        min=4, max=40)])
    
    password = StringField(validators=[DataRequired(), Length(
        min=9, max=40)])
    
    # submit = SubmitField("Register")
    
    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError("Email Address already in use.")

        
class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Length(
        min=4, max=40)])
    
    password = StringField(validators=[DataRequired(), Length(
        min=9, max=40)])
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Email provided does not exist')
        
    def valid_credentials(self, password, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Email provided might not exist')
        if not user.check_password(password):
            raise ValidationError('Credentials provided do not match')
    
    # submit = SubmitField("Log In")    