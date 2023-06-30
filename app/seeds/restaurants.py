# seed restaurants
from app.models import db, Restaurant, environment, SCHEMA
from sqlalchemy.sql import text
def seed_restaurants():
    restaurant1 = Restaurant(
        ownerId = 1,
        name = "Mcdonalds",
        address = "234 Drive",
        cuisineType= "American",
        priceRange = "$",
        imageUrl = "https://b.zmtcdn.com/data/pictures/chains/3/16527533/fa31ad85980e389a91a92f73578bf5b3.jpg?fit=around%7C960:500&crop=960:500;*,*",
        description = "McDonald’s is a global fast food chain known for its iconic golden arches and affordable, convenient menu options."
    )
    restaurant2 = Restaurant(
        ownerId = 2,
        name = "P.F Chang’s",
        address = "224 Drive",
        cuisineType= "Asian",
        priceRange = "$$",
        imageUrl = "https://d1ralsognjng37.cloudfront.net/6a3412c1-fe49-44ce-b1c6-7229f4a94f45.jpeg",
        description = "P.F. Chang’s is a renowned Asian restaurant offering a fusion of flavors and a stylish dining experience."
    )
    restaurant3 = Restaurant(
        ownerId = 3,
        name = "La Trattoria",
        address = "432 Avenue",
        cuisineType= "Italian",
        priceRange = "$$$",
        imageUrl = "https://tb-static.uber.com/prod/image-proc/processed_images/69d46f944e01b0aab20d8173b4be7cd2/16bb0a3ab8ea98cfe8906135767f7bf4.webp",
        description = "La Trattoria is an authentic Italian restaurant offering a delightful menu of traditional dishes and a warm, inviting atmosphere."
    )
    restaurant4 = Restaurant(
        ownerId = 1,
        name = "El Mexicano",
        address = "324 Boulevard",
        cuisineType= "Mexican",
        priceRange = "$$",
        imageUrl = "https://duyt4h9nfnj50.cloudfront.net/resized/1533067443649-w2880-18.jpg",
        description = "El Mexicano is an authentic Mexican restaurant offering a vibrant and flavorful dining experience with a menu full of traditional Mexican favorites."
    )
    restaurant5 = Restaurant(
        ownerId = 2,
        name = "El Sol Mexicano",
        address = "123 Main Street",
        cuisineType = "Mexican",
        priceRange = "$$$",
        imageUrl = "https://duyt4h9nfnj50.cloudfront.net/resized/16f61060f98ded0e3991ebeae0225766-w2880-dc.jpg",
        description = "El Sol Mexicano is a vibrant Mexican restaurant located in the heart of the city. Offering a diverse menu of authentic Mexican dishes, from sizzling fajitas to flavorful enchiladas, it promises a fiesta of flavors. With its lively atmosphere, friendly staff, and excellent service, El Sol Mexicano is a must-visit for Mexican food enthusiasts."
    )
    restaurant6 = Restaurant(
        ownerId = 3,
        name = "La Cantina Mexicana",
        address = "456 Maple Avenue",
        cuisineType = "Mexican",
        priceRange = "$$",
        imageUrl = "https://d1ralsognjng37.cloudfront.net/9ba8dac9-f3d0-4de0-92e1-f9331f040936",
        description = "Experience the true taste of Mexico at La Cantina Mexicana. From mouthwatering tacos to zesty guacamole, their menu showcases the rich and authentic flavors of Mexican cuisine. The cozy and inviting ambiance, coupled with attentive service, creates an enjoyable dining experience. Whether you’re a fan of spicy salsas or refreshing margaritas, La Cantina Mexicana has something to satisfy every craving."
    )
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(restaurant3)
    db.session.add(restaurant4)
    db.session.add(restaurant5)
    db.session.add(restaurant6)
    db.session.commit()
def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))
    db.session.commit()