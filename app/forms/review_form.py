from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    rating = IntegerField('rating', validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])
   