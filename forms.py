from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
from wtforms import RadioField, SubmitField
from wtforms import DateField

class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
   
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])
    gender = RadioField('Gender', choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ])
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
     
     
     