# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length

class MovieForm(FlaskForm):
    class Meta:
        csrf = False
        
    title = StringField(
        'Movie Title',
        validators=[
            DataRequired(message="Title is required."),
            Length(max=100, message="Title must be under 100 characters.")
        ]
    )

    description = TextAreaField(
        'Description',
        validators=[
            DataRequired(message="Please provide a brief description of the movie.")
        ]
    )

    poster = FileField(
        'Movie Poster',
        validators=[
            FileRequired(message="Poster image is required."),
            FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')
        ]
    )
