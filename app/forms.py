from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class addProfile(FlaskForm):

    fname = TextField('First Name', validators=[DataRequired()])
    lname = TextField('Last Name', validators=[DataRequired()])

    gender = SelectField('Gender', choices = [('M', 'Male'), ('F', 'Female')])

    email = TextField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "eg. joe@example.com"})
    
    location = TextField('Location', validators=[DataRequired()], render_kw={"placeholder": "eg. Kingston, Jamaica"})

    biography = TextAreaField('Biography', validators=[DataRequired()])

    propic = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])

    submit = SubmitField('Send')