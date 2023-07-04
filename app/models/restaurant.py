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
    reviews = db.relationship("Review", back_populates="restaurant", cascade="all, delete")
    orders = db.relationship("Order", back_populates="restaurant", cascade="all, delete")
    menuItems = db.relationship("MenuItem", back_populates="restaurant", cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'ownerId': self.ownerId,
            'name': self.name,
            'address': self.address,
            'cuisineType': self.cuisineType,
            'priceRange': self.priceRange,
            'imageUrl': self.imageUrl,
            'description': self.description,
            'rating' : sum([review.rating for review in self.reviews]) / len(self.reviews),
            'reviewCount' : len(self.reviews)
        }
