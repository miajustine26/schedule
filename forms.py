from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TimeField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    #attribute=value('arguments')
    username=StringField('Username', validators=[Length(min=4,max=24), DataRequired()])
    email=StringField('Email', validators=[Length(min=5,max=50), DataRequired(), Email()])
    confirmEmail=StringField('Confirm Email', validators=[DataRequired(), Email(), EqualTo('email')])
    password=PasswordField('Password', validators=[Length(min=4,max=32), DataRequired()])
    confirmPassword=PasswordField('Confirm Password', validators=[Length(min=4,max=32), DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign up')

class LogInForm(FlaskForm):
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

class ScheduleMakerForm(FlaskForm):
    dayOfWeek=StringField('Day of the Week', validators=[DataRequired()])
    periodNumber=IntegerField('Period Number', validators=[DataRequired()])
    start_time = TimeField('Start time')
    duration=IntegerField('Duration (in minutes)', validators=[DataRequired()])
    room=StringField('Room', validators=[DataRequired()])
    teacher=StringField('Teacher', validators=[DataRequired()])
    colorCode=StringField('Color', validators=[DataRequired()])
    addClass=SubmitField('Add another class')
    submit=SubmitField('Save schedule')
