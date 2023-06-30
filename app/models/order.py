from .db import db, environment, SCHEMA, add_prefix_for_prod

class Order(db.Model):
    __tablename__ = 'orders'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    restaurantId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")))
    isCompleted = db.Column(db.Boolean, nullable=False)
    deliveryMethod = db.Column(db.String(255), nullable=False)
    paymentDetails = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, default=db.func.now())

    user = db.relationship("User", back_populates="orders")
    restaurant = db.relationship("Restaurant", back_populates="orders")
    shoppingCarts = db.relationship("ShoppingCart", back_populates="order")

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'restaurantId': self.restaurantId,
            'isCompleted': self.isCompleted,
            'deliveryMethod': self.deliveryMethod,
            'paymentDetails': self.paymentDetails,
            'address': self.address,
            'createdAt': self.createdAt
        }