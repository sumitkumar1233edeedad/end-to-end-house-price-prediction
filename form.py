from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
     
    email = StringField('Email', validators=[DataRequired(message='email message is requjiered'), Email(message='that dose not look like a valid email')])
    submit = SubmitField('register')

    