from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
# from server import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	submit = SubmitField('Take Photo')

	# WTFORMS documentation to validate if user is already within the database
	# https://wtforms.readthedocs.io/en/stable/
	# def validate_username(self, username):
	# 	user = User.query.filter_by(username=username.data).first()
	# 	if user:
	# 		raise ValidationError('Username already exists.')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	submit = SubmitField('Log In')
