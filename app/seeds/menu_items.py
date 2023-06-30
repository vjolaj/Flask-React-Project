from app.models import db, MenuItem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_menuItems():
  
    menuItem1 = MenuItem(
        itemName = "Big Mac",
        restaurantId = 1,
        price = 4.99,
        itemType = "Entree",
        description = "Two all-beef patties, special sauce, lettuce, cheese, pickles, onions on a sesame seed bun.",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_201907_0005_BigMac_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem2 = MenuItem(
        itemName = "McChicken",
        restaurantId = 1,
        price = 3.49,
        itemType = "Entree",
        description = "A crispy chicken patty topped with mayonnaise and shredded lettuce, served on a toasted bun.",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/mcdonalds-McChicken-Sandwich-2:1-3-product-tile-desktop?wid=829&hei=515&dpr=off"
    )

    menuItem3 = MenuItem(
        itemName = "French Fries",
        restaurantId = 1,
        price = 2.49,
        itemType = "Side",
        description = "Golden, crispy, and perfectly salted fries.",
        imageUrl = "https://static.wikia.nocookie.net/legendsofthemultiuniverse/images/8/85/Rs_1024x759-160414152941-rs_1024x759-130926124115-1024-mcdonalds-fries-092613.jpg/revision/latest?cb=20200102171019"
    )

    menuItem4 = MenuItem(
        itemName = "McFlurry",
        restaurantId = 1,
        price = 3.99,
        itemType = "Dessert",
        description = "Soft serve ice cream blended with your choice of mix-ins, like Oreo or M&M's.",
        imageUrl = "https://static.wikia.nocookie.net/ronaldmcdonald/images/0/0a/7008a0028716c9cad1d4bec614663c27.jpg/revision/latest?cb=20190601014324"
    )

    menuItem5 = MenuItem(
        itemName = "Chicken McNuggets",
        restaurantId = 1,
        price = 4.49,
        itemType = "Entree",
        description = "Delicious bite-sized pieces of tender and juicy chicken, coated in a crispy golden breading. Perfectly seasoned and served with your choice of dipping sauces, McDonald's Chicken Nuggets are a classic favorite loved by kids and adults alike.",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/mcdonalds-20-chicken-mcnuggets:1-3-product-tile-desktop?wid=829&hei=515&dpr=off"
    )

    menuItem6 = MenuItem(
        itemName = "Coke",
        restaurantId = 1,
        price = 2.5,
        itemType = "Drink",
        description = "",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem7 = MenuItem(
        itemName = "Mongolian Beef",
        restaurantId = 2,
        price = 14.99,
        itemType = "Entree",
        description = "Tender slices of beef stir-fried with scallions and garlic in a savory soy-based sauce. Served with steamed white rice.",
        imageUrl = "https://www.lecremedelacrumb.com/wp-content/uploads/2021/08/pf-changs-mongolian-beef-14sm-4.jpg"
    )

    menuItem8 = MenuItem(
        itemName = "Kung Pao Chicken",
        restaurantId = 2,
        price = 13.99,
        itemType = "Entree",
        description = "Wok-tossed diced chicken with peanuts, vegetables, and chili peppers in a spicy Kung Pao sauce. Served with your choice of steamed white or brown rice.",
        imageUrl = "https://www.pfchangshomemenu.com/sites/g/files/qyyrlu311/files/uploadedImages/img_8272_30982.jpg"
    )

    menuItem9 = MenuItem(
        itemName = "Shrimp Dumplings",
        restaurantId = 2,
        price = 9.99,
        itemType = "Appetizer",
        description = "Delicate dumplings filled with seasoned shrimp, steamed to perfection. Served with a soy-vinegar dipping sauce.",
        imageUrl = "https://twoplaidaprons.com/wp-content/uploads/2020/05/Chinese-pork-dumplings-picking-up-a-dumpling-with-chopsticks.jpg"
    )

    menuItem10 = MenuItem(
        itemName = "Vegetable Lo Mein",
        restaurantId = 2,
        price = 12.99,
        itemType = "Entree",
        description = "Stir-fried noodles tossed with a medley of fresh vegetables in a flavorful sauce. A satisfying vegetarian option packed with delicious flavors.",
        imageUrl = "https://www.southernplate.com/wp-content/uploads/2020/02/DSC_7306-1-scaled.jpg"
    )

    menuItem11 = MenuItem(
        itemName = "Water",
        restaurantId = 2,
        price = 2.5,
        itemType = "Drink",
        description = "",
        imageUrl = "https://media.officedepot.com/images/f_auto,q_auto,e_sharpen,h_450/products/516125/516125_p/516125"
    )
    
    db.session.add(menuItem1)
    db.session.add(menuItem2)
    db.session.add(menuItem3)
    db.session.add(menuItem4)
    db.session.add(menuItem5)
    db.session.add(menuItem6)
    db.session.add(menuItem7)
    db.session.add(menuItem8)
    db.session.add(menuItem9)
    db.session.add(menuItem10)
    db.session.add(menuItem11)
    db.session.commit()

def undo_menuItems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menuitems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menuItems"))
        
    db.session.commit()

