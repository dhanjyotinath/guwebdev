from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, RadioField, SubmitField, DateField, FileField
from wtforms.validators import DataRequired, NumberRange, Regexp
from flask_wtf.file import FileAllowed

class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    email = EmailField('Email', validators=[
        DataRequired(),
        Regexp(r'^[a-zA-Z0-9._%+-]+@gauhati\.ac\.in$', message="Only @gauhati.ac.in email allowed")
    ])

    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])

    gender = RadioField('Gender', choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ], validators=[DataRequired()])

    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])

    file = FileField('Upload File', validators=[
        DataRequired(),
        FileAllowed(['pdf', 'jpg', 'jpeg'], 'Only PDF and JPG allowed!')
    ])

    submit = SubmitField('Submit')
