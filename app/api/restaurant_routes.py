from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import Restaurant, db, User
from app.forms import RestaurantForm
from .auth_routes import validation_errors_to_error_messages

restaurant_routes = Blueprint("restaurants", __name__)

@restaurant_routes.route('')
def get_all_restaurants():
    restaurants = Restaurant.query.all()
    # return "<h1>Hello from all restaurants</h1>"

    return {"all_restaurants":{restaurant.id: restaurant.to_dict() for restaurant in restaurants} }
  

@restaurant_routes.route('/<int:restaurantId>')
def get_single_restaurant(restaurantId):

    restaurant_info = Restaurant.query.get(restaurantId)
    return {"restaurant_info": restaurant_info.to_dict()}


@restaurant_routes.route('/new', methods=["POST"])
@login_required
def create_restaurant():

    form = RestaurantForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    form.ownerId.data = current_user.id

    if form.validate_on_submit():
        new_restaurant = Restaurant(
            ownerId= current_user.id,
            name=form.data['name'],
            address=form.data['address'],
            cuisineType=form.data['cuisineType'],
            priceRange=form.data['priceRange'],
            imageUrl=form.data['imageUrl'],
            description=form.data['description']
        )
        db.session.add(new_restaurant)
        db.session.commit()
        
        return {"new_restaurant": new_restaurant.to_dict()}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
   
