from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import Restaurant, db, User, Review
from app.forms import RestaurantForm
from .auth_routes import validation_errors_to_error_messages

restaurant_routes = Blueprint("restaurants", __name__)

@restaurant_routes.route('')
def get_all_restaurants():
    """
    This route will return a list of all restaurants.
    """
    restaurants = Restaurant.query.all()
    # return "<h1>Hello from all restaurants</h1>"

    return {"all_restaurants":{restaurant.id: restaurant.to_dict() for restaurant in restaurants} }
  

@restaurant_routes.route('/<int:restaurantId>')
def get_single_restaurant(restaurantId):
    """
    This route will return a restaurant by restaurant Id.
    """
    restaurant_info = Restaurant.query.get(restaurantId)
    return {"restaurant_info": restaurant_info.to_dict()}


@restaurant_routes.route('/new', methods=["POST"])
@login_required
def create_restaurant():
    """
    This route will create a restaurant.
    """
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
   
@restaurant_routes.route('/<int:restaurantId>', methods=["POST"])
@login_required
def update_restaurant(restaurantId):
    # restaurant_to_update = Restaurant.query.get(restaurantId)
    # if restaurant_to_update is None:
    #     return {'errors': ['Restaurant does not exist']}, 404
    """
    This route will update a restaurant (not functional yet).
    """
    form = RestaurantForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    if form.validate_on_submit():
        restaurant_to_update = Restaurant.query.get(restaurantId)
        if restaurant_to_update is None:
            return {'errors': ['Restaurant does not exist']}, 404
        if restaurant_to_update.ownerId is not current_user.id:
            return {'errors': ['Unauthorized access']}, 403
        print(">>>>>>>FORM DATA HEREEEE<<<<<<<<", form.data)
        restaurant_to_update.name = form.data['name']
        restaurant_to_update.address=form.data['address'],
        restaurant_to_update.cuisineType=form.data['cuisineType'],
        restaurant_to_update.priceRange=form.data['priceRange'],
        restaurant_to_update.imageUrl=form.data['imageUrl'],
        restaurant_to_update.description=form.data['description']
        restaurant_to_update.ownerId = current_user.id
        restaurant_to_update.id = restaurantId
        db.session.commit()
        return {"updated_restaurant": restaurant_to_update.to_dict()}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@restaurant_routes.route("/<int:restaurantId>/delete", methods=['DELETE'])
@login_required
def delete_restaurant(restaurantId):
    """
    This route will return a list of restaurants owned by the current user.
    """
    restaurant_to_delete = Restaurant.query.get(restaurantId)

    if restaurant_to_delete is None:
        return {'errors': ['Restaurant does not exist']}, 404
    if restaurant_to_delete.ownerId is not current_user.id:
        return {'errors': ['Unauthorized access']}, 403
    db.session.delete(restaurant_to_delete)
    db.session.commit()
    return {'message': ['Restaurant successfully deleted']}

@restaurant_routes.route("/current")
@login_required
def get_current_restaurants():
    """
    This route will return a list of restaurants owned by the current user.
    """
    current_restaurants = Restaurant.query.filter(Restaurant.ownerId == current_user.id).all()
    return {"current_restaurants": {restaurant.id: restaurant.to_dict() for restaurant in current_restaurants}}

