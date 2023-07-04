from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import Restaurant, db, User, MenuItem, Review
from app.forms import RestaurantForm, MenuItemForm, ReviewForm
from .auth_routes import validation_errors_to_error_messages
from .AWS_helpers import get_unique_filename, upload_file_to_s3, remove_file_from_s3

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
    This route will delete a restaurant.
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

@restaurant_routes.route("/<int:restaurantId>/menu-items", methods=['GET', 'POST'])
@login_required
def edit_menu_items(restaurantId):
    """
    This route will both and get and add menu items to a restaurant.
    """
    restaurant = Restaurant.query.get(restaurantId)
    if restaurant is None:
        return {'errors': ['Restaurant does not exist']}, 404
    
    if restaurant.ownerId is not current_user.id:
        return {'errors': ['Unauthorized access']}, 403
    
    restaurant_menu_items = MenuItem.query.filter(MenuItem.restaurantId == restaurantId).all()

    form = MenuItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    if form.validate_on_submit():
        image = form.data["imageUrl"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
       
        new_menu_item = MenuItem(
            restaurantId= restaurantId,
            itemName=form.data['itemName'],
            price=form.data['price'],
            itemType=form.data['itemType'],
            description=form.data['description'],
            imageUrl= upload['url']
        )
        db.session.add(new_menu_item)
        db.session.commit()
        
        return {"new_menu_item": new_menu_item.to_dict()}
    if form.errors:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    
    return {"restaurant_menu_items": {menuItem.id: menuItem.to_dict() for menuItem in restaurant_menu_items}}

#Get all reviews of single restaurant
@restaurant_routes.route("/<int:restaurantId>/reviews")
def get_reviews_single_restaurant(restaurantId):
    restaurant = Restaurant.query.get(restaurantId)
    reviews = Review.query.filter_by(restaurantId = restaurantId)
    return {"restaurant_reviews":{review.id: review.to_dict() for review in reviews}}

#Get all reviews    
@restaurant_routes.route("/reviews")
def get_all_reviews():
    reviews = Review.query.all()
    return {"restaurant_reviews":{review.id: review.to_dict() for review in reviews}}

#POST a new review
@restaurant_routes.route("/<int:restaurantId>/reviews/new", methods=['POST'])
@login_required
def create_review(restaurantId):
    restaurant = Restaurant.query.get(restaurantId)
    form=ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
  
    if form.validate_on_submit():
        new_review = Review(
            restaurantId = restaurant.id,
            userId = current_user.id,
            rating = form.data['rating'],
            description= form.data['description']
        )

        db.session.add(new_review)
        db.session.commit()
        
        return {"new_review": new_review.to_dict()}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
