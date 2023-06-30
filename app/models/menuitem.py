from .db import db, environment, SCHEMA, add_prefix_for_prod

class MenuItem(db.Model):
    __tablename__ = 'menuItems'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(50), nullable=False)
    restaurantId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")))
    price = db.Column(db.Float, nullable=False)
    itemType = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    imageUrl = db.Column(db.String(255))
    
    restaurant = db.relationship("Restaurant", back_populates="menuItems")
    shoppingCarts = db.relationship("ShoppingCart", secondary="shoppingCart_menuItems", back_populates="menuItem")
    

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