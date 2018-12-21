from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
	firstName=StringField('First Name', validators=[DataRequired(), Length(min=1, max=25)])
	lastName=StringField('Last Name', validators=[DataRequired(), Length(min=1, max=25)])
	contactEmail=StringField('Email Address', validators=[DataRequired(), Email()])
	submit=SubmitField('Submit')