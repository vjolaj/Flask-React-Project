from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Order, User, MenuItem, OrderItem

orders_routes = Blueprint("orders", __name__)

@orders_routes.route('/current')
def get_users_orders():
    """
    This route will return a list of all past orders of the current logged in user.
    """
    print('backend hit, requesting...')
    print(current_user)
    orders = Order.query.filter(Order.userId == current_user.id and Order.isCompleted == True).all()

    return {
        "users_orders": {
            order.id: order.to_dict() for order in orders
        }
    }

@orders_routes.route('/<int:orderId>/menuItem', methods=['DELETE'])
@login_required
def remove_item_from_order(orderId):
    req = request.get_json()
    # menuItemId = req["menuItemId"]
    # menuItem = MenuItem.query.get(menuItemId)
    item = OrderItem.query.filter(OrderItem.orderId == orderId).filter(OrderItem.menuItemId == req['menuItemId']).first()

    db.session.delete(item)
    db.session.commit()
    order = Order.query.get(orderId)
    if len(order.menuItems) == 0:
        order.restaurantId = 0
        db.session.commit

    return order.to_dict()

@orders_routes.route('/<int:orderId>/menuItem', methods=['POST'])
# @login_required
def add_item_to_order(orderId):
    """
    This route adds an item and its quantity to current order (cart)
    """
    req = request.get_json()
    order = Order.query.get(orderId)
    menuItemId = req["menuItemId"]
    quantity = req['quantity']
    print("***********************", menuItemId, quantity)
    menuItem = MenuItem.query.get(menuItemId)
    if not order.restaurantId or order.restaurantId == 0:
        order.restaurantId = menuItem.restaurantId
    item = OrderItem.query.filter(OrderItem.orderId == orderId).filter(OrderItem.menuItemId == menuItemId).first()
    print(item)

    if item is None:
        order.menuItems.append({"item": menuItem, "amount": quantity})
    else:
        item.quantity += quantity
    db.session.commit()
    return order.to_dict()

@orders_routes.route('/<int:orderId>', methods=['PUT'])
@login_required
def edit_order(orderId):
    """
    This route will finalize orders if isCompleted is passed through, else it will update quantity of items
    """
    order = Order.query.get(orderId)
    req = request.get_json()

    isCompleted = req['isCompleted']

    if isCompleted:
        order.deliveryMethod = req["deliveryMethod"]
        order.paymentDetails = req["paymentDetails"]
        order.isCompleted = True
        order.address = req["address"]
        order.orderedAt = db.func.now()
    else:
        item = OrderItem.query.filter(OrderItem.orderId == req['orderId']).filter(OrderItem.menuItemId == req['menuItemId']).first()

        item.quantity = req['quantity']

    db.session.commit()
    return order.to_dict()
