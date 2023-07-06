from flask import Blueprint, session
from app.models import User, db, Order
from flask_login import current_user

cart_routes = Blueprint("cart", __name__)

@cart_routes.route('/new-order', methods=['POST'])
def new_order():
    """
    Creates an empty order to be used as the new shopping cart
    """
    print('Creating new cart for ', current_user)
    cart = Order(
        userId = current_user.id,
        isCompleted = False
    )
    print(cart)
    db.session.add(cart)
    db.session.commit()

    return cart.to_dict()

@cart_routes.route('')
def get_cart():
    """
    Gets the logged in users shopping cart
    """
    order = Order.query.filter(Order.userId == current_user.id and Order.isCompleted == False).first()

    return order.to_dict()