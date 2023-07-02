from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class RestaurantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    address = StringField('Address', validators=[DataRequired(), Length(max=255)])
    cuisineType = SelectField('Cuisine Type', choices=[('American', 'American'), ('Asian', 'Asian'), ('Italian', 'Italian'), ('Mexican', 'Mexican'), ('Seafood', 'Seafood'), ('Pizza','Pizza')])
    priceRange = SelectField('Price Range', choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$'), ('$$$$', '$$$$')])
    imageUrl = StringField('ImageUrl', validators=[DataRequired(), Length(max=255)])
    description = StringField('Description', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Submit')



