from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.ext.associationproxy import association_proxy
from .orderItem import OrderItem

class Order(db.Model):
    __tablename__ = 'orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    restaurantId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")))
    isCompleted = db.Column(db.Boolean, nullable=False)
    deliveryMethod = db.Column(db.String(255))
    paymentDetails = db.Column(db.String(255))
    address = db.Column(db.String(255))
    orderedAt = db.Column(db.DateTime)
    totalPrice = db.Column(db.Numeric)

    user = db.relationship("User", back_populates="orders")
    restaurant = db.relationship("Restaurant", back_populates="orders")
    # orderItems = db.relationship("OrderItem", back_populates="order", cascade="all, delete")
    # menuItems = db.relationship("MenuItem", secondary="OrderItem", back_populates="orders")
    menuItemAssociation = db.relationship("OrderItem", back_populates="order", cascade="all, delete")
    menuItems = association_proxy("menuItemAssociation", 'menuItem', creator=lambda input: OrderItem(menuItem=input['item'], quantity=input['amount']))
    # *In theory* should be able to add menuItems in the format of:
    #           new_menuItem = MenuItem(
    #               'itemName': request.json.get('itemName'),
    #               'restaurantId': request.json.get('restaurantId'),
    #               'price': request.json.get('price'),
    #               'itemType': request.json.get('itemType'),
    #               'description': request.json.get('description'),
    #               'imageUrl': request.json.get('imageUrl'),
    #           )
    #           current_order.menuItems.append(new_menuItem)
    #
    #  quantity is set to default to 1, but *in theory* can pass in optional second argument to set the quantity:
    #           current_order.menuItems.append(new_menuItem, 3)
    #
    #  further adjustments to quantity will need to be done directly to the orderItems table:
    #           current_orderItem.quantity = 4

    def to_dict(self):
        items = {orderItem.menuItemId : dict(orderItem.to_dict()['MenuItem'], **{'quantity' : orderItem.to_dict()['quantity']}) for orderItem in self.menuItemAssociation}

        return {
            'id': self.id,
            'userId': self.userId,
            'restaurantId': self.restaurantId,
            'isCompleted': self.isCompleted,
            'deliveryMethod': self.deliveryMethod,
            'paymentDetails': self.paymentDetails,
            'address': self.address,
            'orderedAt': self.orderedAt,
            'Items' : items,
            'totalItems' : sum([item['quantity'] for item in items.values()]),
            'totalCost' : sum([item['price'] * item['quantity'] for item in items.values()]),
            'totalPrice': self.totalPrice
        }
