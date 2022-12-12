from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class ArtForm(FlaskForm):
    picture = FileField('Upload Your Artwork', validators=[FileAllowed(['jpg', 'png'])])
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
    artist = StringField('Artist', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update')