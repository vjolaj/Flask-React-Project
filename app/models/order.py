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

    user = db.relationship("User", back_populates="orders")
    restaurant = db.relationship("Restaurant", back_populates="orders")
    # orderItems = db.relationship("OrderItem", back_populates="order", cascade="all, delete")
    # menuItems = db.relationship("MenuItem", secondary="OrderItem", back_populates="orders")
    menuItemAssociation = db.relationship("OrderItem", back_populates="order")
    menuItems = association_proxy("menuItemAssociation", 'menuItem', creator=lambda item: OrderItem(menuItem=item))


    def to_dict(self):
        items = {orderItem.menuItemId : dict(orderItem.MenuItem, **{'quantity' : orderItem.quantity}) for orderItem in self.orderItems}

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
            'TotalItems' : sum([item.quantity for item in items])
        }
