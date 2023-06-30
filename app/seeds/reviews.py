from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    review1 = Review(
        restaurantId = 2,
        userId = 2,
        rating = 5,
        description = "Absolutely phenomenal! The food was a culinary delight, with each dish bursting with exquisite flavors. The service was impeccable, with attentive staff going above and beyond to ensure a memorable dining experience. Highly recommended!"
    )

    review2 = Review(
        restaurantId = 4,
        userId = 2,
        rating = 5,
        description = "Absolutely phenomenal! The food was a culinary delight, with each dish bursting with exquisite flavors. The service was impeccable, with attentive staff going above and beyond to ensure a memorable dining experience. Highly recommended!"
    )

    review3 = Review(
        restaurantId = 1,
        userId = 3,
        rating = 2,
        description = "Disappointing visit. The food was bland and lacked any distinct taste. The service was slow, and the staff seemed uninterested in catering to our needs. Overall, a forgettable experience that didn't live up to expectations."
    )

    review4 = Review(
        restaurantId = 3,
        userId = 2,
        rating = 4,
        description = "Great place for a casual meal! The food was delicious and reasonably priced. The atmosphere was relaxed and inviting, perfect for catching up with friends or enjoying a laid-back evening. I'll definitely be coming back!"
    )

    review5 = Review(
        restaurantId = 1,
        userId = 5,
        rating = 1,
        description = "Worst experience ever! The food was tasteless and seemed to have been reheated multiple times. The service was incredibly slow, and the staff was rude and unprofessional. I wouldn't recommend this place to anyone."
    )


    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()  
