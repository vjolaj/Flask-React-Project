# from app.models import db, orderItem, environment, SCHEMA
# from sqlalchemy.sql import text

# def seed_order_item():
#     item1 = orderItem(
#         orderId= 1,
#         menuItemId = 57,
#         quantity = 2,
#     )

#     item2 = orderItem(
#         orderId= 1,
#         menuItemId = 65,
#         quantity = 1,
#     )

#     db.session.add(item1)
#     db.session.add(item2)
#     db.session.commit()

# def undo_order_item():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.orderitems RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM orderitems"))
        
#     db.session.commit()
