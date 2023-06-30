from .db import db, environment, SCHEMA, add_prefix_for_prod

class ShoppingCart(db.Model):
    __tablename__ = 'shoppingCarts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("orders.id")))
    quantity = db.Column(db.Integer, nullable=False)

    menuItems = db.relationship("MenuItem",secondary= "shoppingCart_menuItems", back_populates="shoppingCart")
    order = db.relationship("Order", back_populates="shoppingCart")

    def to_dict(self):
        return {
            'id': self.id,
            'orderId': self.orderId,
            'quantity': self.quantity,
            'Items': { menuItem.id: menuItem.to_dict() for menuItem in self.menuItems}

        }

