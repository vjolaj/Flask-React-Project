from .db import db, environment, SCHEMA, add_prefix_for_prod

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    cuisineType = db.Column(db.String(40), nullable=False)
    priceRange = db.Column(db.String, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    
    
    owner = db.relationship("User", back_populates="restaurants")
    reviews = db.relationship("Review", back_populates="restaurant")
    orders = db.relationship("Order", back_populates="restaurant")
    menuItems = db.relationship("MenuItem", back_populates="restaurant")
    
    def to_dict(self):
        return {
            'id': self.id,
            'ownerId': self.ownerId,
            'name': self.name,
            'address': self.address,
            'cuisineType': self.cuisineType,
            'priceRange': self.priceRange,
            'imageUrl': self.imageUrl,
            'rating': self.rating,
            'description': self.description
        }