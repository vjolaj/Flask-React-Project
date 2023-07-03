from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Order, User, MenuItem

orders_routes = Blueprint("orders", __name__)

@orders_routes.route('/current')
def get_users_orders():
    """
    This route will return a list of all past orders of the current logged in user.
    """
    orders = Order.query.filter(Order.userId == current_user.id and Order.isCompleted == True).all()
    print(orders)

    return {
        "users_orders": {
            order.id: order.to_dict() for order in orders
        }
    }

# @orders_routes.route('')