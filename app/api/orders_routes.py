from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Order, User, MenuItem

orders_routes = Blueprint("orders", __name__)

@orders_routes.route('/current')
def get_users_orders():
    """
    This route will return a list of all past orders of the current logged in user.
    """
    print('backend hit, requesting...')
    print(current_user)
    orders = Order.query.filter(Order.userId == current_user.id and Order.isCompleted == True).all()
    print('****************', orders)

    return {
        "users_orders": {
            order.id: order.to_dict() for order in orders
        }
    }


@orders_routes.route('/<int:orderId>', methods=['PUT'])
@login_required
def edit_order(orderId):
    order = Order.query.get(orderId)
    req = request.get_json()

    new_delivery_method = req["deliveryMethod"]
    new_paymentDetails = req["paymentDetails"]
    new_address = req["address"]
    completed = req["isCompleted"]

    if new_delivery_method:
        order.deliveryMethod = new_delivery_method
    if new_paymentDetails:
        order.paymentDetails = new_paymentDetails
    if new_address:
        order.address = new_address
    if completed:
        order.isCompleted = True
        order.orderedAt = db.func.now()

    db.session.commit()
    return order.to_dict()

@orders_routes.route('/<int:orderId>', methods=['POST'])
@login_required
def add_item_to_order(orderId):
    req = request.json()
    order = Order.query.get(orderId)
    menuItemId = req["menuItemId"]
    menuItem = MenuItem.query.get(menuItemId)
    order.append(menuItem)
    db.session.commit()
    return order.to_dict()

@orders_routes.route('/<int:orderId>/menuItem', methods=['Delete'])
@login_required
def add_item_to_order(orderId):
    req = request.json()
    order = Order.query.get(orderId)
    menuItemId = req["menuItemId"]
    menuItem = MenuItem.query.get(menuItemId)
    order.menuItems.remove(menuItem)
    db.session.commit()
    return order.to_dict()


# @orders_routes.route('')
