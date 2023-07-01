from .db import db, environment, SCHEMA, add_prefix_for_prod
from .shoppingcart_menuitem import shoppingCart_menuItems

class ShoppingCart(db.Model):
    __tablename__ = 'shopping_carts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("orders.id")))
    quantity = db.Column(db.Integer, nullable=False)

    menuItems = db.relationship("MenuItem",secondary= shoppingCart_menuItems, back_populates="shoppingCarts")
    order = db.relationship("Order", back_populates="shoppingCarts")

    def to_dict(self):
        return {
            'id': self.id,
            'orderId': self.orderId,
            'quantity': self.quantity,
        }

