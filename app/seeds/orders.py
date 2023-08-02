from app.models import db, Order, environment, SCHEMA
from sqlalchemy.sql import text

def seed_order():
    order1 = Order(
       userId = 1,
       isCompleted= False,
       deliveryMethod = "delivery",
       paymentDetails = "PayPal",
       address = "321 Drive"
    )

    order2 = Order(
        userId = 2,
        isCompleted = False,
        deliveryMethod = "delivery",
        paymentDetails = "Credit Card",
        address = "456 Main Street"
    )

    order3 = Order(
        userId = 3,
        isCompleted = False,
        deliveryMethod = "pickup",
        paymentDetails = "Cash",
        address = "673 Drive"
    )

    # order4 = Order(
    #    userId = 1,
    #    restaurantId = 5,
    #    isCompleted= True,
    #    deliveryMethod = "Delivery",
    #    paymentDetails = "Visa",
    #    address = "321 Drive",
    #    totalPrice = 25.86
    # )
    

    # db.session.add(order4)
    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)
    db.session.commit()

def undo_order():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orders"))
        
    db.session.commit()

