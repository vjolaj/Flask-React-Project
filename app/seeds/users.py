from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', firstName='Demo', lastName='User', phoneNumber=1234567890)
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', firstName='Marnie', lastName='Shelton', phoneNumber=1234567891)
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', firstName='Bobbie', lastName='Millar', phoneNumber=1234567892)
    user2 = User(
        username='user2', email='user2@aa.io', password='password', firstName='John', lastName='Doe', phoneNumber=1234567893)
    user3 = User(
        username='user3', email='user3@aa.io', password='password', firstName='Alice', lastName='Johnson', phoneNumber=1234567894)
    user4 = User(
        username='user4', email='user4@aa.io', password='password', firstName='Michael', lastName='Smith', phoneNumber=1234567895)
    user5 = User(
        username='user5', email='user5@aa.io', password='password', firstName='Emily', lastName='Brown', phoneNumber=1234567896)
    user6 = User(
        username='user6', email='user6@aa.io', password='password', firstName='Daniel', lastName='Lee', phoneNumber=1234567897)
    user7 = User(
        username='user7', email='user7@aa.io', password='password', firstName='Sophia', lastName='Wang', phoneNumber=1234567898)
    user8 = User(
        username='user8', email='user8@aa.io', password='password', firstName='Oliver', lastName='Garcia', phoneNumber=1234567899)
    user9 = User(
        username='user9', email='user9@aa.io', password='password', firstName='Isabella', lastName='Lopez', phoneNumber=1234567900)
    user10 = User(
        username='user10', email='user10@aa.io', password='password', firstName='William', lastName='Chen', phoneNumber=1234567901)
    user11 = User(
        username='user11', email='user11@aa.io', password='password', firstName='Ava', lastName='Nguyen', phoneNumber=1234567902)
    user12 = User(
        username='user12', email='user12@aa.io', password='password', firstName='James', lastName='Kim', phoneNumber=1234567903)
    
    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)
    db.session.add(user11)
    db.session.add(user12)
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()