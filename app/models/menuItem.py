from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.ext.associationproxy import association_proxy
from .orderItem import OrderItem

class MenuItem(db.Model):
    __tablename__ = 'menuitems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    restaurantId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")))
    price = db.Column(db.Numeric(4, 2), nullable=False)
    itemType = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    imageUrl = db.Column(db.String(255))

    restaurant = db.relationship("Restaurant", back_populates="menuItems")
    # orderItems = db.relationship("OrderItem", back_populates="menuItem", cascade="all, delete")
    # orders = db.relationship("Order", secondary="OrderItem", back_populates="menuItems")
    orderAssociation = db.relationship("OrderItem", back_populates="menuItem", cascade="all, delete")
    orders = association_proxy("orderAssociation", 'order', creator=lambda o: OrderItem(order=o))

    def to_dict(self):
        return {
            'id': self.id,
            'itemName': self.itemName,
            'restaurantId': self.restaurantId,
            'price': self.price,
            'itemType': self.itemType,
            'description': self.description,
            'imageUrl': self.imageUrl
        }
