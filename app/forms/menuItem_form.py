from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.AWS_helpers import ALLOWED_EXTENSIONS

def price_within_range(form, field):
    #Checking if price is within $0 to $100
    price = field.data
    if price < 0 or price > 99.99:
        raise ValidationError("Price must be within $0 and $99.99.")
    
class MenuItemForm(FlaskForm):
    itemName = StringField('Item Name', validators=[DataRequired(), Length(max=255)])
    price = DecimalField('Price', validators=[DataRequired(), price_within_range])
    itemType = SelectField('Item Type', choices=[('Entree', 'Entree'), ('Side', 'Side'), ('Dessert', 'Dessert'), ('Drink', 'Drink')])
    description = StringField('Item description', validators=[DataRequired(), Length(max=255)])
    imageUrl = FileField("Item Image", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])

