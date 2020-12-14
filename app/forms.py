from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from .models import User

class LoginForm(FlaskForm):
    username = StringField('username ')
    password = PasswordField('password ')
    submit = SubmitField('Login')