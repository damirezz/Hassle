from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from qanda.models import User

class RegistrationForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired(), Regexp('^[A-Za-z]{3,}$',
                message='First name can only contain letters')])
    lname = StringField('Last Name', validators=[DataRequired(), Regexp('^[A-Za-z]{3,}$',
                message='Last name can only contain letters')])
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email address')])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, message='Phone Number is too short'), Regexp('^[0-9]{3,}$',
                message='Invalid Phone Number')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'confirm_password', message="Password Must Match"
    )])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    

    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValueError('This Email Has Been Used')
    
    def validate_phone(self, phone):
        phone = User.query.filter_by(phone = phone.data).first()
        if phone:
            raise ValueError('This Phone Number Has Been Used Registered by Another User') 

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email address')])

    password = PasswordField('Password', validators=[DataRequired()])

class UpdateAccountInfo(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired(), Regexp('^[A-Za-z]{3,}$',
                message='First name can only contain letters')])
    lname = StringField('Last Name', validators=[DataRequired(), Regexp('^[A-Za-z]{3,}$',
                message='Last name can only contain letters')])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, message='Phone Number is too short'), Regexp('^[0-9]{3,}$',
                message='Invalid Phone Number')])