from .db import db, environment, SCHEMA, add_prefix_for_prod

class OrderItem(db.Model):
    __tablename__ = 'orderitems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("orders.id")))
    menuItemId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("menuitems.id")))
    quantity = db.Column(db.Integer, default=1, nullable=False)

    # menuItem = db.relationship("MenuItem", back_populates="orderItems")
    # order = db.relationship("Order", back_populates="orderItems")
    menuItem = db.relationship('MenuItem', back_populates='orderAssociation')
    order = db.relationship('Order', back_populates='menuItemAssociation')

    def to_dict(self):
        return {
            'id': self.id,
            'orderId': self.orderId,
            'menuItemId': self.menuItemId,
            'quantity': self.quantity,
            'MenuItem': self.menuItem.to_dict()
        }
