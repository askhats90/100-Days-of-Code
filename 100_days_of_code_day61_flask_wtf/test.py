from wtforms import StringField, PasswordField, SubmitField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField(label='Log In')
