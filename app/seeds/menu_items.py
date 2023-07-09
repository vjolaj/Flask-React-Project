from app.models import db, MenuItem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_menu_items():

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
        imageUrl = "https://acclaimmag.com/wp-content/uploads/2014/07/FriesCova.jpg"
    )

    menuItem4 = MenuItem(
        itemName = "McFlurry",
        restaurantId = 1,
        price = 3.99,
        itemType = "Dessert",
        description = "Soft serve ice cream blended with your choice of mix-ins, like Oreo or M&M's.",
        imageUrl = "https://hips.hearstapps.com/hmg-prod/images/screen-shot-2019-08-26-at-1-02-16-pm-1566838950.png"
    )

    menuItem5 = MenuItem(
        itemName = "Chicken McNuggets",
        restaurantId = 1,
        price = 4.49,
        itemType = "Entree",
        description = "Delicious bite-sized pieces of tender and juicy chicken, coated in a crispy golden breading.",
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
        itemType = "Entree",
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
        itemName = "White Rice",
        restaurantId = 2,
        price = 3.50,
        itemType = "Side",
        description = "Bowl of white rice",
        imageUrl = "https://static01.nyt.com/images/2018/02/21/dining/00RICEGUIDE8/00RICEGUIDE8-superJumbo.jpg"
    )

    menuItem12 = MenuItem(
        itemName = "Fried Rice",
        restaurantId = 2,
        price = 5.99,
        itemType = "Side",
        description = "Chicken Fried Rice",
        imageUrl = "https://www.licious.in/blog/wp-content/uploads/2022/12/Shutterstock_1043177881.jpg"
    )

    menuItem13 = MenuItem(
        itemName = "Water",
        restaurantId = 2,
        price = 2.5,
        itemType = "Drink",
        description = "Bottle of water",
        imageUrl = "https://media.officedepot.com/images/f_auto,q_auto,e_sharpen,h_450/products/516125/516125_p/516125"
    )

    menuItem14 = MenuItem(
        itemName = "Coke",
        restaurantId = 2,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )


    menuItem15 = MenuItem(
        itemName = "Ice Cream",
        restaurantId = 2,
        price = 5.99,
        itemType = "Dessert",
        description = "Chocolate Ice Cream",
        imageUrl = "https://joyfoodsunshine.com/wp-content/uploads/2020/06/homemade-chocolate-ice-cream-recipe-7.jpg"
    )

    menuItem16 = MenuItem(
        itemName = "CheeseCake",
        restaurantId = 2,
        price = 4.50,
        itemType = "Dessert",
        description = "Strawberry ChesseCake",
        imageUrl = "https://sugargeekshow.com/wp-content/uploads/2022/12/cherry_cheesecake_featured-4-of-6-copy.jpg"
    )

    menuItem17 = MenuItem(
        itemName="Spaghetti Carbonara",
        restaurantId=3,
        price=12.99,
        itemType="Entree",
        description="Classic Italian pasta dish with bacon, eggs, and Parmesan cheese.",
        imageUrl="https://twoplaidaprons.com/wp-content/uploads/2020/07/spaghetti-carbonara-top-down-view-of-a-nest-of-carbonara-with-an-egg-yolk-500x375.jpg"
    )

    menuItem18 = MenuItem(
        itemName="Margherita Pizza",
        restaurantId=3,
        price=10.99,
        itemType="Entree",
        description="Traditional Neapolitan pizza with fresh tomatoes, mozzarella cheese, and basil.",
        imageUrl="https://www.blossmangas.com/wp-content/uploads/2021/05/Margherita-pizza-2.jpg"
    )
    menuItem19 = MenuItem(
        itemName="Lasaga",
        restaurantId=3,
        price=15.99,
        itemType="Entree",
        description="Fresh tomatoes, mozzarella cheese, and basil.",
        imageUrl="https://www.unileverfoodsolutions.com.ph/dam/global-ufs/mcos/SEA/calcmenu/recipes/PH-recipes/the-vegetarian-butcher/lasagna/1245x600_Lasagna.jpg"
    )

    menuItem20 = MenuItem(
        itemName="Bruschetta",
        restaurantId=3,
        price=8.99,
        itemType="Side",
        description="Toasted bread topped with fresh tomatoes, garlic, and basil.",
        imageUrl="https://www.theedgyveg.com/wp-content/uploads/2021/07/Vegan-Bruschetta-1.jpg"
    )

    menuItem21 = MenuItem(
        itemName="Caprese Salad",
        restaurantId=3,
        price=9.99,
        itemType="Side",
        description="Sliced tomatoes, fresh mozzarella, and basil, drizzled with olive oil.",
        imageUrl="https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2019/07/Caprese-Salad-main-1.jpg"
    )


    menuItem22 = MenuItem(
        itemName="Tiramisu",
        restaurantId=3,
        price=6.99,
        itemType="Dessert",
        description="Layers of coffee-soaked ladyfingers and mascarpone cream, dusted with cocoa powder.",
        imageUrl="https://www.kingarthurbaking.com/sites/default/files/2023-03/Tiramisu_1426.jpg"
    )

    menuItem23 = MenuItem(
        itemName="Cannoli",
        restaurantId=3,
        price=5.99,
        itemType="Dessert",
        description="Crisp pastry tubes filled with sweetened ricotta cheese and chocolate chips.",
        imageUrl="https://www.momontimeout.com/wp-content/uploads/2021/04/churro-cannolis-square.jpeg"
    )

    menuItem24 = MenuItem(
        itemName="Espresso",
        restaurantId=3,
        price=2.99,
        itemType="Drink",
        description="Strong black coffee served in a small cup.",
        imageUrl="https://thumbs.dreamstime.com/b/espresso-shot-glass-white-background-42113855.jpg"
    )

    menuItem25 = MenuItem(
        itemName = "Coke",
        restaurantId = 3,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem26 = MenuItem(
        itemName="Chicken Tacos",
        restaurantId=4,
        price=14.99,
        itemType="Entree",
        description="Corn tortillas filled with seasoned shredded chicken, topped with enchilada sauce and melted cheese.",
        imageUrl="https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2021/04/Easy-Ground-Beef-Tacos-edit-40.jpg"
    )

    menuItem27 = MenuItem(
        itemName="Beef Tacos",
        restaurantId=4,
        price=12.99,
        itemType="Entree",
        description="Soft or crispy tortillas filled with seasoned ground beef, lettuce, tomato, and cheese.",
        imageUrl="https://feelgoodfoodie.net/wp-content/uploads/2017/04/Ground-Beef-Tacos-9.jpg"
    )

    menuItem28 = MenuItem(
        itemName="Guacamole",
        restaurantId=4,
        price=7.99,
        itemType="Side",
        description="Mashed avocado mixed with lime juice, onions, tomatoes, and cilantro.",
        imageUrl="https://www.santitas.com/sites/santitas.com/files/2023-03/guacamole-recipes-detail.png"
    )

    menuItem29 = MenuItem(
        itemName="Mexican Rice",
        restaurantId=4,
        price=4.99,
        itemType="Side",
        description="Fluffy rice cooked with tomatoes, onions, and spices.",
        imageUrl="https://shelfcooking.com/wp-content/uploads/2020/09/Mexican-Rice-Recipe.jpg"
    )

    menuItem30 = MenuItem(
        itemName="Churros",
        restaurantId=4,
        price=6.99,
        itemType="Dessert",
        description="Deep-fried dough pastry sprinkled with cinnamon sugar, served with chocolate dipping sauce.",
        imageUrl="https://cafedelites.com/wp-content/uploads/2020/05/Churros-Recipe-IMAGE-124.jpg"
    )

    menuItem31 = MenuItem(
        itemName="Flan",
        restaurantId=4,
        price=5.99,
        itemType="Dessert",
        description="Creamy caramel custard dessert with a caramelized sugar topping.",
        imageUrl="https://www.lactaid.com/sites/lactaid_us/files/recipe-images/easy_flan2.jpg"
    )

    menuItem32 = MenuItem(
        itemName = "Coke",
        restaurantId = 4,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem33 = MenuItem(
        itemName="Sprite",
        restaurantId=4,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem34 = MenuItem(
        itemName="Deluxe Sandwich",
        restaurantId=5,
        price=6.50,
        itemType="Entree",
        description="Chicken, tomatoes and lettuce sandwich",
        imageUrl="https://www.hamburgerstand.com/wp-content/uploads/2015/03/deluxe-chicken-schnitzel.jpg"
    )

    menuItem35 = MenuItem(
        itemName="Spicy Sandwich",
        restaurantId=5,
        price=7.50,
        itemType="Entree",
        description="Spicy Sanwich with lettuce and tomatoes",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/DC_202104_0100_DeluxeSpicyCrispyChickenSandwich_PotatoBun_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem36 = MenuItem(
        itemName="Fries",
        restaurantId=5,
        price=3.99,
        itemType="Side",
        description="French Fries",
        imageUrl="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/Small_Lowered_1217shoot_1080x1080.png"
    )

    menuItem37 = MenuItem(
        itemName="Chicken Nuggets",
        restaurantId=5,
        price=5.99,
        itemType="Side",
        description="12 Chicken nuggets",
        imageUrl="https://www.wbrc.com/resizer/ztr0Sf97wlXOGQZdvPH6anwn7EE=/300x0/arc-photo-gray/arc3-prod/public/NK7JJVEDJBD5ZDNLZDYGOC42W4.png"
    )

    menuItem38 = MenuItem(
        itemName="Ice Cream",
        restaurantId=5,
        price=2.50,
        itemType="Dessert",
        description="Vanilla Ice Cream",
        imageUrl="https://www.cfacdn.com/img/order/menu/Online/Sides%26treats/IceDream_RedCup_1080x1080.png"
    )

    menuItem39 = MenuItem(
        itemName="Brownie",
        restaurantId=5,
        price=2.50,
        itemType="Dessert",
        description="Chocolate Brownie",
        imageUrl="https://d1fd34dzzl09j.cloudfront.net/2020/September/CFA%20Chocolate%20Fudge%20Brownie1_700_by_587.jpg"
    )

    menuItem40 = MenuItem(
        itemName = "Coke",
        restaurantId = 5,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem41 = MenuItem(
        itemName="Sprite",
        restaurantId=5,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem42 = MenuItem(
        itemName="Crunchy Taco",
        restaurantId=6,
        price=1.99,
        itemType="Entree",
        description="Crispy corn taco shell filled with seasoned beef, lettuce, and cheese.",
        imageUrl="https://www.fastfoodmenuprices.com/wp-content/uploads/2013/07/3-crunchy-tacos.png"
    )

    menuItem43 = MenuItem(
        itemName="Quesadilla",
        restaurantId=6,
        price=3.99,
        itemType="Entree",
        description="Grilled flour tortilla filled with melted cheese and your choice of protein.",
        imageUrl="https://www.tacobell.com/images/22320_cheese_quesadilla_750x660.jpg"
    )

    menuItem44 = MenuItem(
        itemName="Cheesy Fiesta Potatoes",
        restaurantId=6,
        price=2.99,
        itemType="Side",
        description="Crispy potatoes seasoned with a blend of cheeses and spices.",
        imageUrl="https://www.tacobell.com/images/22530_cheesy_fiesta_potatoes_750x660.jpg"
    )

    menuItem45 = MenuItem(
        itemName="Nachos Supreme",
        restaurantId=6,
        price=4.99,
        itemType="Side",
        description="Tortilla chips topped with seasoned beef, nacho cheese sauce, tomatoes, and sour cream.",
        imageUrl="https://www.taketwotapas.com/wp-content/uploads/2022/03/Nachos-Supreme-RS-Take-Two-Tapas-12.jpg"
    )

    menuItem46 = MenuItem(
        itemName="Cinnamon Twists",
        restaurantId=6,
        price=1.99,
        itemType="Dessert",
        description="Sweet and crunchy cinnamon-flavored twists.",
        imageUrl="https://copykat.com/wp-content/uploads/2023/03/Taco-Bell-Cinnamon-Twists-Photo-4.jpg"
    )

    menuItem47 = MenuItem(
        itemName="Caramel Apple Empanada",
        restaurantId=6,
        price=2.49,
        itemType="Dessert",
        description="Fried pastry filled with diced apples and sweet caramel sauce.",
        imageUrl="https://hips.hearstapps.com/hmg-prod/images/empanada-1564691224.png"
    )

    menuItem48 = MenuItem(
        itemName = "Coke",
        restaurantId = 6,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem49 = MenuItem(
        itemName="Sprite",
        restaurantId=6,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem50 = MenuItem(
        itemName="Hamburger",
        restaurantId=7,
        price=6.99,
        itemType="Entree",
        description="Fresh ground beef patty with your choice of toppings.",
        imageUrl="https://d2luv1saso99wi.cloudfront.net/2022_Digital-Menu_Burgers_ShackBurger_1500x920_lg1663589553.jpeg"
    )

    menuItem51 = MenuItem(
        itemName="Bacon Cheeseburger",
        restaurantId=7,
        price=8.99,
        itemType="Entree",
        description="Hamburger topped with crispy bacon and melted cheese.",
        imageUrl="https://d2luv1saso99wi.cloudfront.net/2022_Digital-Menu_Burgers_BaconCheeseburger_1500x920_lg1663591000.jpeg"
    )

    menuItem52 = MenuItem(
        itemName="Fries",
        restaurantId=7,
        price=3.49,
        itemType="Side",
        description="Seasoned fries with a spicy Cajun seasoning.",
        imageUrl="https://cdn.britannica.com/34/206334-050-7637EB66/French-fries.jpg"
    )

    menuItem53 = MenuItem(
        itemName="Cheese Dog",
        restaurantId=7,
        price=5.99,
        itemType="Side",
        description="Grilled hot dog topped with melted cheese.",
        imageUrl="https://www.soulfullymade.com/wp-content/uploads/2022/07/baked-chili-cheese-dogs-square.jpg"
    )

    menuItem54 = MenuItem(
        itemName="Milkshake",
        restaurantId=7,
        price=4.99,
        itemType="Dessert",
        description="Creamy milkshake in your choice of flavor.",
        imageUrl="https://pbs.twimg.com/media/DpTYw-cXgAAkdvB.jpg"
    )

    menuItem55 = MenuItem(
        itemName = "Ice Cream",
        restaurantId = 7,
        price = 5.99,
        itemType = "Dessert",
        description = "Chocolate Ice Cream",
        imageUrl = "https://joyfoodsunshine.com/wp-content/uploads/2020/06/homemade-chocolate-ice-cream-recipe-7.jpg"
    )

    menuItem56 = MenuItem(
        itemName="Sprite",
        restaurantId=7,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem57 = MenuItem(
        itemName = "Coke",
        restaurantId = 7,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem58 = MenuItem(
        itemName="Hamburger",
        restaurantId=8,
        price=6.99,
        itemType="Entree",
        description="Fresh ground beef patty with your choice of toppings.",
        imageUrl="https://d2luv1saso99wi.cloudfront.net/2022_Digital-Menu_Burgers_ShackBurger_1500x920_lg1663589553.jpeg"
    )

    menuItem59 = MenuItem(
        itemName="Bacon Cheeseburger",
        restaurantId=8,
        price=8.99,
        itemType="Entree",
        description="Hamburger topped with crispy bacon and melted cheese.",
        imageUrl="https://d2luv1saso99wi.cloudfront.net/2022_Digital-Menu_Burgers_BaconCheeseburger_1500x920_lg1663591000.jpeg"
    )

    menuItem60 = MenuItem(
        itemName="Fries",
        restaurantId=8,
        price=3.49,
        itemType="Side",
        description="Seasoned fries with a spicy Cajun seasoning.",
        imageUrl="https://d2luv1saso99wi.cloudfront.net/2022_Digital-Menu_CrinkleCutFries_Fries_1500x920_lg1663591933.jpeg"
    )

    menuItem61 = MenuItem(
        itemName="Hot Dog",
        restaurantId=8,
        price=5.99,
        itemType="Side",
        description="Grilled hot dog",
        imageUrl="https://d2luv1saso99wi.cloudfront.net/2022_Digital-Menu_FlatTopDogs_HotDog_1500x920_lg1663589845.jpeg"
    )

    menuItem62 = MenuItem(
        itemName="Milkshake",
        restaurantId=8,
        price=4.99,
        itemType="Dessert",
        description="Creamy milkshake in your choice of flavor.",
        imageUrl="https://assets3.thrillist.com/v1/image/3132928/828x610/flatten;crop;webp=auto;jpeg_quality=60.jpg"
    )

    menuItem63 = MenuItem(
        itemName = "Ice Cream",
        restaurantId = 8,
        price = 5.99,
        itemType = "Dessert",
        description = "Chocolate Ice Cream",
        imageUrl = "https://vegnews.com/media/W1siZiIsIjM3Nzc4L1ZlZ05ld3MuVmVnYW5DdXN0YXJkLlNoYWtlU2hhY2suanBnIl0sWyJwIiwidGh1bWIiLCIxMzYweCIseyJmb3JtYXQiOm51bGx9XSxbInAiLCJvcHRpbWl6ZSJdXQ/VegNews.VeganCustard.ShakeShack.jpg?sha=80e1c6e578a907bc"
    )

    menuItem64 = MenuItem(
        itemName="Sprite",
        restaurantId=8,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )


    menuItem65 = MenuItem(
        itemName = "Coke",
        restaurantId = 8,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem66 = MenuItem(
        itemName="Chicken Tacos",
        restaurantId=9,
        price=14.99,
        itemType="Entree",
        description="Corn tortillas filled with seasoned shredded chicken, topped with enchilada sauce and melted cheese.",
        imageUrl="https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2021/04/Easy-Ground-Beef-Tacos-edit-40.jpg"
    )

    menuItem67 = MenuItem(
        itemName="Beef Tacos",
        restaurantId=9,
        price=12.99,
        itemType="Entree",
        description="Soft or crispy tortillas filled with seasoned ground beef, lettuce, tomato, and cheese.",
        imageUrl="https://feelgoodfoodie.net/wp-content/uploads/2017/04/Ground-Beef-Tacos-9.jpg"
    )

    menuItem68 = MenuItem(
        itemName="Guacamole",
        restaurantId=9,
        price=7.99,
        itemType="Side",
        description="Mashed avocado mixed with lime juice, onions, tomatoes, and cilantro.",
        imageUrl="https://www.santitas.com/sites/santitas.com/files/2023-03/guacamole-recipes-detail.png"
    )

    menuItem69 = MenuItem(
        itemName="Mexican Rice",
        restaurantId=9,
        price=4.99,
        itemType="Side",
        description="Fluffy rice cooked with tomatoes, onions, and spices.",
        imageUrl="https://shelfcooking.com/wp-content/uploads/2020/09/Mexican-Rice-Recipe.jpg"
    )

    menuItem70 = MenuItem(
        itemName="Churros",
        restaurantId=9,
        price=6.99,
        itemType="Dessert",
        description="Deep-fried dough pastry sprinkled with cinnamon sugar, served with chocolate dipping sauce.",
        imageUrl="https://cafedelites.com/wp-content/uploads/2020/05/Churros-Recipe-IMAGE-124.jpg"
    )

    menuItem71 = MenuItem(
        itemName="Flan",
        restaurantId=9,
        price=5.99,
        itemType="Dessert",
        description="Creamy caramel custard dessert with a caramelized sugar topping.",
        imageUrl="https://www.lactaid.com/sites/lactaid_us/files/recipe-images/easy_flan2.jpg"
    )

    menuItem72 = MenuItem(
        itemName = "Coke",
        restaurantId = 9,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem73 = MenuItem(
        itemName="Sprite",
        restaurantId=9,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem74 = MenuItem(
        itemName="Chicken Tacos",
        restaurantId=10,
        price=14.99,
        itemType="Entree",
        description="Corn tortillas filled with seasoned shredded chicken, topped with enchilada sauce and melted cheese.",
        imageUrl="https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2021/04/Easy-Ground-Beef-Tacos-edit-40.jpg"
    )

    menuItem75 = MenuItem(
        itemName="Beef Tacos",
        restaurantId=10,
        price=12.99,
        itemType="Entree",
        description="Soft or crispy tortillas filled with seasoned ground beef, lettuce, tomato, and cheese.",
        imageUrl="https://feelgoodfoodie.net/wp-content/uploads/2017/04/Ground-Beef-Tacos-9.jpg"
    )

    menuItem76 = MenuItem(
        itemName="Guacamole",
        restaurantId=10,
        price=7.99,
        itemType="Side",
        description="Mashed avocado mixed with lime juice, onions, tomatoes, and cilantro.",
        imageUrl="https://www.santitas.com/sites/santitas.com/files/2023-03/guacamole-recipes-detail.png"
    )

    menuItem77 = MenuItem(
        itemName="Mexican Rice",
        restaurantId=10,
        price=4.99,
        itemType="Side",
        description="Fluffy rice cooked with tomatoes, onions, and spices.",
        imageUrl="https://shelfcooking.com/wp-content/uploads/2020/09/Mexican-Rice-Recipe.jpg"
    )

    menuItem78 = MenuItem(
        itemName="Churros",
        restaurantId=10,
        price=6.99,
        itemType="Dessert",
        description="Deep-fried dough pastry sprinkled with cinnamon sugar, served with chocolate dipping sauce.",
        imageUrl="https://cafedelites.com/wp-content/uploads/2020/05/Churros-Recipe-IMAGE-124.jpg"
    )

    menuItem79 = MenuItem(
        itemName="Flan",
        restaurantId=10,
        price=5.99,
        itemType="Dessert",
        description="Creamy caramel custard dessert with a caramelized sugar topping.",
        imageUrl="https://www.lactaid.com/sites/lactaid_us/files/recipe-images/easy_flan2.jpg"
    )

    menuItem80 = MenuItem(
        itemName = "Coke",
        restaurantId =10,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem81 = MenuItem(
        itemName="Sprite",
        restaurantId= 10,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem82 = MenuItem(
        itemName="Hamburger",
        restaurantId=11,
        price=6.99,
        itemType="Entree",
        description="Fresh ground beef patty with your choice of toppings.",
        imageUrl="https://www.in-n-out.com/ResourcePackages/INNOUT/content/images/menu/cheeseburger-meal.png?package=INNOUT&v=2023"
    )

    menuItem83 = MenuItem(
        itemName="Bacon Cheeseburger",
        restaurantId=11,
        price=8.99,
        itemType="Entree",
        description="Hamburger topped with crispy bacon and melted cheese.",
        imageUrl="https://d2luv1saso99wi.cloudfront.net/2022_Digital-Menu_Burgers_BaconCheeseburger_1500x920_lg1663591000.jpeg"
    )

    menuItem84 = MenuItem(
        itemName="Fries",
        restaurantId=11,
        price=3.49,
        itemType="Side",
        description="Seasoned fries.",
        imageUrl="https://www.mashed.com/img/gallery/the-truth-about-in-n-out-fries/intro-1584565796.jpg"
    )

    menuItem85 = MenuItem(
        itemName="Cheese Dog",
        restaurantId=11,
        price=5.99,
        itemType="Side",
        description="Grilled hot dog topped with melted cheese.",
        imageUrl="https://www.soulfullymade.com/wp-content/uploads/2022/07/baked-chili-cheese-dogs-square.jpg"
    )

    menuItem86 = MenuItem(
        itemName="Milkshake",
        restaurantId=11,
        price=4.99,
        itemType="Dessert",
        description="Creamy milkshake in your choice of flavor.",
        imageUrl="https://assets.change.org/photos/5/ak/sl/MXakslArwJgqthV-800x450-noPad.jpg?1485746442"
    )

    menuItem87 = MenuItem(
        itemName = "Ice Cream",
        restaurantId =11,
        price = 5.99,
        itemType = "Dessert",
        description = "Chocolate Ice Cream",
        imageUrl = "https://joyfoodsunshine.com/wp-content/uploads/2020/06/homemade-chocolate-ice-cream-recipe-7.jpg"
    )

    menuItem88 = MenuItem(
        itemName="Sprite",
        restaurantId=11,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )


    menuItem89 = MenuItem(
        itemName = "Coke",
        restaurantId = 11,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem90 = MenuItem(
        itemName="Chicken Tacos",
        restaurantId=12,
        price=14.99,
        itemType="Entree",
        description="Corn tortillas filled with seasoned shredded chicken, topped with enchilada sauce and melted cheese.",
        imageUrl="https://www.fromvalerieskitchen.com/wordpress/wp-content/uploads/2021/04/Easy-Ground-Beef-Tacos-edit-40.jpg"
    )

    menuItem91 = MenuItem(
        itemName="Beef Tacos",
        restaurantId=12,
        price=12.99,
        itemType="Entree",
        description="Soft or crispy tortillas filled with seasoned ground beef, lettuce, tomato, and cheese.",
        imageUrl="https://feelgoodfoodie.net/wp-content/uploads/2017/04/Ground-Beef-Tacos-9.jpg"
    )

    menuItem92 = MenuItem(
        itemName="Guacamole",
        restaurantId=12,
        price=7.99,
        itemType="Side",
        description="Mashed avocado mixed with lime juice, onions, tomatoes, and cilantro.",
        imageUrl="https://www.santitas.com/sites/santitas.com/files/2023-03/guacamole-recipes-detail.png"
    )

    menuItem93 = MenuItem(
        itemName="Mexican Rice",
        restaurantId=12,
        price=4.99,
        itemType="Side",
        description="Fluffy rice cooked with tomatoes, onions, and spices.",
        imageUrl="https://shelfcooking.com/wp-content/uploads/2020/09/Mexican-Rice-Recipe.jpg"
    )

    menuItem94 = MenuItem(
        itemName="Churros",
        restaurantId=12,
        price=6.99,
        itemType="Dessert",
        description="Deep-fried dough pastry sprinkled with cinnamon sugar, served with chocolate dipping sauce.",
        imageUrl="https://cafedelites.com/wp-content/uploads/2020/05/Churros-Recipe-IMAGE-124.jpg"
    )

    menuItem95 = MenuItem(
        itemName="Flan",
        restaurantId=12,
        price=5.99,
        itemType="Dessert",
        description="Creamy caramel custard dessert with a caramelized sugar topping.",
        imageUrl="https://www.lactaid.com/sites/lactaid_us/files/recipe-images/easy_flan2.jpg"
    )

    menuItem96 = MenuItem(
        itemName = "Coke",
        restaurantId =12,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem97 = MenuItem(
        itemName="Sprite",
        restaurantId= 12,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem98 = MenuItem(
        itemName="Sushi Platter",
        restaurantId=13,
        price=44.99,
        itemType="Entree",
        description="Assortment of sushi rolls including California roll, spicy tuna roll, and salmon roll.",
        imageUrl="https://static.wixstatic.com/media/a73f49_4c6cf9102945499081f6f9b96ee988fa~mv2.jpg/v1/crop/x_1152,y_0,w_5887,h_5464/fill/w_422,h_390,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/OsakaPlatterTray%5BHeroShot%5D_JPG.jpg"
    )

    menuItem99 = MenuItem(
        itemName="Spicy Tuna Roll",
        restaurantId=13,
        price=14.99,
        itemType="Entree",
        description="Fresh Spicy Tuna Roll.",
        imageUrl="https://www.tiger-corporation.com/wp-content/uploads/2023/02/hero-img-recipe-spicy-tuna-3db6e125056f2bde01321a3da5d290da.jpg"
    )

    menuItem100 = MenuItem(
        itemName="Miso Soup",
        restaurantId=13,
        price=3.99,
        itemType="Side",
        description="Traditional Japanese soup made with miso paste, tofu, and seaweed.",
        imageUrl="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Miso_Soup_001.jpg/1200px-Miso_Soup_001.jpg"
    )

    menuItem101 = MenuItem(
        itemName="Gyoza",
        restaurantId=13,
        price=6.99,
        itemType="Side",
        description="Pan-fried Japanese dumplings filled with ground pork and vegetables.",
        imageUrl="https://cardamommagazine.com/wp-content/uploads/2021/04/chicken-gyoza.jpg"
    )

    menuItem102 = MenuItem(
        itemName="Tempura Ice Cream",
        restaurantId=13,
        price=7.99,
        itemType="Dessert",
        description="Fried ice cream wrapped in a crispy tempura shell, served with a drizzle of chocolate sauce.",
        imageUrl="https://kitchenfunwithmy3sons.com/wp-content/uploads/2022/04/fried-ice-cream-feature.jpg"
    )

    menuItem103 = MenuItem(
        itemName = "Ice Cream",
        restaurantId =13,
        price = 5.99,
        itemType = "Dessert",
        description = "Chocolate Ice Cream",
        imageUrl = "https://joyfoodsunshine.com/wp-content/uploads/2020/06/homemade-chocolate-ice-cream-recipe-7.jpg"
    )

    menuItem104 = MenuItem(
        itemName="Sprite",
        restaurantId=13,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem105 = MenuItem(
        itemName = "Coke",
        restaurantId = 13,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem106 = MenuItem(
        itemName="Orange Chicken",
        restaurantId=14,
        price=12.99,
        itemType="Entree",
        description="Crispy chicken pieces tossed in a tangy and sweet orange sauce.",
        imageUrl="https://www.modernhoney.com/wp-content/uploads/2018/01/Chinese-Orange-Chicken-2.jpg"
    )

    menuItem107 = MenuItem(
        itemName="Kung Pao Shrimp",
        restaurantId=14,
        price=14.99,
        itemType="Entree",
        description="Stir-fried shrimp with peanuts, vegetables, and spicy Kung Pao sauce.",
        imageUrl="https://www.joyousapron.com/wp-content/uploads/2019/08/Kung-Pao-Shrimp-Sq-Pic.jpg"
    )

    menuItem108 = MenuItem(
        itemName="Egg Rolls",
        restaurantId=14,
        price=5.99,
        itemType="Side",
        description="Fried rolls filled with cabbage, carrots, and other vegetables, served with sweet and sour sauce.",
        imageUrl="https://dinnersdishesanddesserts.com/wp-content/uploads/2021/12/Vietnamese-Egg-Rolls-square-scaled.jpg"
    )

    menuItem109 = MenuItem(
        itemName="Fried Rice",
        restaurantId=14,
        price=8.99,
        itemType="Side",
        description="Classic Chinese dish made with stir-fried rice, vegetables, and choice of protein.",
        imageUrl="https://www.everydayeasyeats.com/wp-content/uploads/2016/06/Chinese-Fried-Rice-3.jpg"
    )

    menuItem110 = MenuItem(
        itemName="Sesame Balls",
        restaurantId=14,
        price=2.99,
        itemType="Dessert",
        description="Classic Chinese dish made with stir-fried rice, vegetables, and choice of protein.",
        imageUrl="https://takestwoeggs.com/wp-content/uploads/2022/02/Sesame-Balls-with-red-bean-paste-sq-500x500.jpg"
    )

    menuItem111 = MenuItem(
        itemName = "Ice Cream",
        restaurantId = 14,
        price = 5.99,
        itemType = "Dessert",
        description = "Chocolate Ice Cream",
        imageUrl = "https://joyfoodsunshine.com/wp-content/uploads/2020/06/homemade-chocolate-ice-cream-recipe-7.jpg"
    )

    menuItem112 = MenuItem(
        itemName="Sprite",
        restaurantId= 14,
        price=2.5,
        itemType="Drink",
        description="Regular Sprite",
        imageUrl="https://s7d1.scene7.com/is/image/mcdonalds/Header_MediumSprite_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem113 = MenuItem(
        itemName = "Coke",
        restaurantId = 14,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem114 = MenuItem(
        itemName = "Mongolian Beef",
        restaurantId = 15,
        price = 14.99,
        itemType = "Entree",
        description = "Tender slices of beef stir-fried with scallions and garlic in a savory soy-based sauce. Served with steamed white rice.",
        imageUrl = "https://www.lecremedelacrumb.com/wp-content/uploads/2021/08/pf-changs-mongolian-beef-14sm-4.jpg"
    )

    menuItem115 = MenuItem(
        itemName = "Kung Pao Chicken",
        restaurantId = 15,
        price = 13.99,
        itemType = "Entree",
        description = "Wok-tossed diced chicken with peanuts, vegetables, and chili peppers in a spicy Kung Pao sauce. Served with your choice of steamed white or brown rice.",
        imageUrl = "https://www.pfchangshomemenu.com/sites/g/files/qyyrlu311/files/uploadedImages/img_8272_30982.jpg"
    )

    menuItem116 = MenuItem(
        itemName = "Shrimp Dumplings",
        restaurantId = 15,
        price = 9.99,
        itemType = "Entree",
        description = "Delicate dumplings filled with seasoned shrimp, steamed to perfection. Served with a soy-vinegar dipping sauce.",
        imageUrl = "https://twoplaidaprons.com/wp-content/uploads/2020/05/Chinese-pork-dumplings-picking-up-a-dumpling-with-chopsticks.jpg"
    )

    menuItem117 = MenuItem(
        itemName = "Vegetable Lo Mein",
        restaurantId = 15,
        price = 12.99,
        itemType = "Entree",
        description = "Stir-fried noodles tossed with a medley of fresh vegetables in a flavorful sauce. A satisfying vegetarian option packed with delicious flavors.",
        imageUrl = "https://www.southernplate.com/wp-content/uploads/2020/02/DSC_7306-1-scaled.jpg"
    )

    menuItem118 = MenuItem(
        itemName = "White Rice",
        restaurantId = 15,
        price = 3.50,
        itemType = "Side",
        description = "Bowl of white rice",
        imageUrl = "https://static01.nyt.com/images/2018/02/21/dining/00RICEGUIDE8/00RICEGUIDE8-superJumbo.jpg"
    )

    menuItem119 = MenuItem(
        itemName = "Fried Rice",
        restaurantId = 15,
        price = 5.99,
        itemType = "Side",
        description = "Chicken Fried Rice",
        imageUrl = "https://www.licious.in/blog/wp-content/uploads/2022/12/Shutterstock_1043177881.jpg"
    )

    menuItem120 = MenuItem(
        itemName = "Water",
        restaurantId = 15,
        price = 2.5,
        itemType = "Drink",
        description = "Bottle of water",
        imageUrl = "https://media.officedepot.com/images/f_auto,q_auto,e_sharpen,h_450/products/516125/516125_p/516125"
    )

    menuItem121 = MenuItem(
        itemName = "Coke",
        restaurantId = 15,
        price = 2.5,
        itemType = "Drink",
        description = "Regular Coke",
        imageUrl = "https://s7d1.scene7.com/is/image/mcdonalds/DC_202112_0521_MediumCoke_Glass_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off"
    )

    menuItem151 = MenuItem(
        itemName = "Cheese Sticks",
        restaurantId = 16,
        price = 7.19,
        itemType = "Side",
        description = "A side everyone can agree on! Get these cheese sticks sprinkled with flavorful Italian seasoning and a cup of our delicious marinara.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127486661836677231/Screenshot_2023-07-09_at_2.28.25_AM.png"
    )

    menuItem152 = MenuItem(
        itemName = "Breadsticks",
        restaurantId = 16,
        price = 5.99,
        itemType = "Side",
        description = "Nobody does breadsticks like the Hut. Crispy-on-the-outside, soft-on-the-inside, and seasoned with garlic and parmesan, they're perfect with pizza or pasta. Comes with a cup of our delicious marinara!",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127486662205767720/Screenshot_2023-07-09_at_2.28.56_AM.png"
    )

    menuItem153 = MenuItem(
        itemName = "Pepperoni Lover's® Pizza",
        restaurantId = 16,
        price = 21.59,
        itemType = "Entree",
        description = "The classic 1-topping pepperoni pizza you crave, loaded up with 50% more pepperoni.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127487747263840396/1628637276856.jpeg"
    )

    menuItem154 = MenuItem(
        itemName = "Buffalo Chicken Pizza",
        restaurantId = 16,
        price = 21.59,
        itemType = "Entree",
        description = "We took your favorite food and put it on a pizza. With tangy buffalo sauce, tender chicken and banana peppers, this beautiful masterpiece tastes like a football game feels.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127487747494514758/cover_image.jpg.760x400_q85_crop_upscale.jpg"
    )

    menuItem155 = MenuItem(
        itemName = "Cinnabon® Mini Rolls",
        restaurantId = 16,
        price = 8.39,
        itemType = "Dessert",
        description = "10 mini cinnamon rolls, topped with signature cream cheese frosting, are the perfect way to end pizza night. Or you can eat 'em first. Don't worry, we won't tell.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127488686217502792/dessert.cinnabon-mini-rolls.7e98475ca6dd067f5b6e327ab0d9a788.1.jpg"
    )

    menuItem156 = MenuItem(
        itemName = "Triple Chocolate Brownie",
        restaurantId = 16,
        price = 8.99,
        itemType = "Dessert",
        description = "Chocolate, chocolate, and more chocolate. Dig into this rich, decadent brownie made with semi-sweet chocolate, dark chocolate and cocoa. Did we mention there's chocolate?",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127488685961658439/20-1555339742.jpg"
    )

    menuItem157 = MenuItem(
        itemName = "Cheesesticks",
        restaurantId = 17,
        price = 8.99,
        itemType = "Side",
        description = "Original fresh dough covered with Special Garlic sauce, topped with mounds of real cheese made from mozzarella, then baked to a cheesy, gooey goodness. Served with original pizza sauce for dipping!",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127486661836677231/Screenshot_2023-07-09_at_2.28.25_AM.png"
    )

    menuItem158 = MenuItem(
        itemName = "Garlic Parmesan Breadsticks",
        restaurantId = 17,
        price = 7.49,
        itemType = "Side",
        description = "Fresh dough baked to a golden brown then topped with our Special Garlic sauce and Parmesan cheese. Served with original pizza sauce for dipping.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127486662205767720/Screenshot_2023-07-09_at_2.28.56_AM.png"
    )

    menuItem159 = MenuItem(
        itemName = "Ultimate Pepperoni Pizza",
        restaurantId = 17,
        price = 14.49,
        itemType = "Entree",
        description = "Just when you think our pepperoni pizza couldn’t get any tastier, we craft the ultimate masterpiece. Our original fresh dough is covered with signature pizza sauce, 30% more pepperoni than our traditional pie, a blend of Parmesan and Romano, and real cheese made from mozzarella, all sprinkled with classic Italian seasoning.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127487747263840396/1628637276856.jpeg"
    )

    menuItem160 = MenuItem(
        itemName = "Chicken Alfredo Papa Bowl",
        restaurantId = 17,
        price = 8.49,
        itemType = "Entree",
        description = "No crust – just an oven-baked bowl of creamy alfredo and garlic parmesan sauces and juicy grilled chicken complemented by spinach, mushrooms, onions, and tomatoes, and topped with a melty three cheese blend and Italian seasoning. *Italian Seasoning contains gluten",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127489965224374312/papajon_bowl.webp"
    )

    menuItem264 = MenuItem(
        itemName = "OREO® Cookie Papa Bites",
        restaurantId = 17,
        price = 6.49,
        itemType = "Dessert",
        description = "Eight sweet bites of OREO® Cookie wrapped in our original fresh dough and drizzled in icing. Baked fresh and served with cream cheese icing dipping sauce on the side.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127490530356502528/papajohn_oreo.jpeg"
    )

    menuItem161 = MenuItem(
        itemName = "Pepsi Zero Sugar",
        restaurantId = 16,
        price = 2.54,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491260157014147/pepsi.jpeg"
    )

    menuItem162 = MenuItem(
        itemName = "Mountain Dew",
        restaurantId = 16,
        price = 2.54,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259301376081/mountain_dew.webp"
    )

    menuItem163 = MenuItem(
        itemName = "Pepsi Zero Sugar",
        restaurantId = 17,
        price = 2.54,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491260157014147/pepsi.jpeg"
    )

    menuItem164 = MenuItem(
        itemName = "Mountain Dew",
        restaurantId = 17,
        price = 2.54,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259301376081/mountain_dew.webp"
    )

    menuItem165 = MenuItem(
        itemName = "Classic Bruschetta",
        restaurantId = 18,
        price = 10.00,
        itemType = "Side",
        description = "Classic tomato & basil.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127492732236079164/bruschetta.jpeg"
    )

    menuItem166 = MenuItem(
        itemName = "Meatball Sliders",
        restaurantId = 18,
        price = 13.00,
        itemType = "Side",
        description = "Grimaldi's meatballs topped with melted mozzarella cheese in Grimaldi's homemade rolls, coated in our homemade Grimaldi's Tomato basil sauce.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127492731904725152/-Cheesy-Meatball-Sliders-_EXPS_GBBZ20_199855_E10_15_3b.jpg"
    )

    menuItem167 = MenuItem(
        itemName = "Brooklyn Bridge Pizza",
        restaurantId = 18,
        price = 22.00,
        itemType = "Entree",
        description = "Oven-roasted red peppers, creamy ricotta cheese, and hand pinched Italian sausage atop our traditional pizza.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127487747263840396/1628637276856.jpeg"
    )

    menuItem168 = MenuItem(
        itemName = "The Grimaldi's Meat Lover's Pizza",
        restaurantId = 18,
        price = 13.00,
        itemType = "Entree",
        description = "Meatballs, pepperoni, Italian sausage, bacon, and ham.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127487747494514758/cover_image.jpg.760x400_q85_crop_upscale.jpg"
    )

    menuItem169 = MenuItem(
        itemName = "Traditional Cannoli",
        restaurantId = 18,
        price = 10.00,
        itemType = "Dessert",
        description = "Delicious tube of fried dough, filled with a sweet, creamy ricotta filling.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127494119418241074/cannoli.jpeg"
    )

    menuItem170 = MenuItem(
        itemName = "Chocolate Mudd Pie Truffle",
        restaurantId = 18,
        price = 10.00,
        itemType = "Dessert",
        description = "Mudd Pie Gelato Fudge Center Dipped in Dark Chocolate.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127493974211440650/mudd_pie.jpeg"
    )

    menuItem171 = MenuItem(
        itemName = "Coca Cola",
        restaurantId = 18,
        price = 2.50,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem172 = MenuItem(
        itemName = "Dasani Water",
        restaurantId = 18,
        price = 2.50,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem173 = MenuItem(
        itemName = "DORITOS® Nacho Cheese",
        restaurantId = 19,
        price = 1.69,
        itemType = "Side",
        description = "The iconic bold and intense cheesiness of Doritos® Nacho Cheese Flavored Tortilla Chips. Doritos® flavors ignite adventure and inspire action. Are you ready? If so, crunch on.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127494980139753502/doritos.jpeg"
    )

    menuItem174 = MenuItem(
        itemName = "SunChips® Harvest Cheddar®",
        restaurantId = 19,
        price = 1.69,
        itemType = "Side",
        description = "The flavor of real cheddar cheese is layered onto a delicious whole grain chip to create this tasty combination.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127494979833573386/sunchips.jpeg"
    )

    menuItem175 = MenuItem(
        itemName = "Buffalo Chicken",
        restaurantId = 19,
        price = 9.99,
        itemType = "Entree",
        description = "When you’re looking to spice things up, do it with Frank’s RedHot® and buffalo chicken. Our Buffalo Chicken Footlong is made with everyone’s favorite hot sauce – Frank’s RedHot® and topped with peppercorn ranch. Try it with lettuce, tomatoes and cucumbers!",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496407402676254/subway_1.jpeg"
    )

    menuItem176 = MenuItem(
        itemName = "Italian B.M.T.®",
        restaurantId = 19,
        price = 8.79,
        itemType = "Entree",
        description = "The Italian B.M.T.® sandwich is filled with Genoa salami, spicy pepperoni, and Black Forest ham. Big. Meaty. Tasty. Get it.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496407662735411/subway2.jpeg"
    )

    menuItem177 = MenuItem(
        itemName = "Chocolate Chip",
        restaurantId = 19,
        price = 0.89,
        itemType = "Dessert",
        description = "One bite of our Chocolate Chip Cookie and you may just find the sudden urge to order 2, 3… maybe 6. It has semi-sweet chocolate chips, vanilla and other natural flavors folded into buttery cookie dough. It’s waiting to be devoured, just don’t say we didn’t warn you!",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496801138770030/Single-Serve-Chocolate-Chip-Cookie-5-735x1103.webp"
    )

    menuItem178 = MenuItem(
        itemName = "Coca-Cola® Classic",
        restaurantId = 19,
        price = 2.99,
        itemType = "Drink",
        description = "Crisp, refreshing, original taste.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem179 = MenuItem(
        itemName = "Dasani® Water",
        restaurantId = 19,
        price = 2.69,
        itemType = "Drink",
        description = "As delicious as our sandwiches are, they are even better when paired with the perfect side and drink or even adding a little something extra. With such a variety to choose from, there's truly something for every taste.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem180 = MenuItem(
        itemName = "BBQ Chips",
        restaurantId = 20,
        price = 2.15,
        itemType = "Side",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127498322958090290/bbq_chips.webp"
    )

    menuItem181 = MenuItem(
        itemName = "Jalapeno Chips",
        restaurantId = 20,
        price = 2.15,
        itemType = "Side",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127498323318808656/jalapeno_chips.jpeg"
    )

    menuItem182 = MenuItem(
        itemName = "Italian Club",
        restaurantId = 20,
        price = 9.99,
        itemType = "Entree",
        description = "SALAMI, CAPOCOLLO, HAM & PROVOLONE onion, lettuce, tomato, mayo, oil & vinegar, & oregano-basil",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496407662735411/subway2.jpeg"
    )

    menuItem183 = MenuItem(
        itemName = "Spicy Italian",
        restaurantId = 20,
        price = 9.99,
        itemType = "Entree",
        description = "DOUBLE GENOA SALAMI, DOUBLE CAPOCOLLO & PROVOLONE hot peppers, sauce, onion, lettuce, tomato & easy mayo (GUTTED) Boom. Good as it gets!",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496407402676254/subway_1.jpeg"
    )

    menuItem184 = MenuItem(
        itemName = "Choc Chip Cookie",
        restaurantId = 20,
        price = 2.35,
        itemType = "Dessert",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127499284682649661/jj_chocolate_chip.jpg"
    )

    menuItem185 = MenuItem(
        itemName = "Coke (Bottle)",
        restaurantId = 20,
        price = 2.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem186 = MenuItem(
        itemName = "Bottled Water",
        restaurantId = 20,
        price = 1.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem187 = MenuItem(
        itemName = "Chicken Pot Pie Soup",
        restaurantId = 21,
        price = 6.79,
        itemType = "Side",
        description = "Tender, slow-roasted chicken breast and delicious veggies with a flaky crumb topping",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127655943790927882/Potbellys-Chicken-Pot-Pie-Soup-Recipe-e1662659767311.jpg"
    )

    menuItem188 = MenuItem(
        itemName = "Garden Vegetable Soup",
        restaurantId = 21,
        price = 6.79,
        itemType = "Side",
        description = "Beans, carrots, celery, corn, mushrooms, onions, peppers, potatoes and zucchini in a light tomato broth",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127655944059371621/potbely_soup.jpeg"
    )

    menuItem189 = MenuItem(
        itemName = "Roast Beef",
        restaurantId = 21,
        price = 9.79,
        itemType = "Entree",
        description = "Angus roast beef, provolone",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127655945024065597/POTBELLY_SANDWICH1.jpeg"
    )

    menuItem190 = MenuItem(
        itemName = "Italian",
        restaurantId = 21,
        price = 10.79,
        itemType = "Entree",
        description = "Salami, old-world capicola, pepperoni, mortadella, provolone",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127655945363791972/Potbelly-feature.jpg"
    )

    menuItem191 = MenuItem(
        itemName = "OREO® Cookie Shake",
        restaurantId = 21,
        price = 7.59,
        itemType = "Dessert",
        description = "Made with hand-dipped ice cream. OREO is a trademark of Mondelez International group, used under license.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127657505305133137/oreo_cookie_shake.jpeg"
    )

    menuItem192 = MenuItem(
        itemName = "Chocolate Brownie Cookie",
        restaurantId = 21,
        price = 3.29,
        itemType = "Entree",
        description = "Baked fresh daily",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127657505015742474/choco_brownie_cookie.jpeg"
    )

    menuItem193 = MenuItem(
        itemName = "Coke",
        restaurantId = 21,
        price = 4.59,
        itemType = "Drink",
        description = "20 oz. Bottle",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem194 = MenuItem(
        itemName = "Bottled Water",
        restaurantId = 21,
        price = 3.19,
        itemType = "Drink",
        description = "25 oz. Bottle",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem195 = MenuItem(
        itemName = "Caesars Special Salad",
        restaurantId = 22,
        price = 15.39,
        itemType = "Side",
        description = "Crisp, delicious romaine lettuce topped with baked croutons shaved parmesan cheese, with a Caesar dressing.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127659623848091808/caesar_salad.jpeg"
    )

    menuItem196 = MenuItem(
        itemName = "Signature Antipasto Salad",
        restaurantId = 22,
        price = 15.39,
        itemType = "Side",
        description = "Salad loaded with meats, cheese and veggies with Italian dressing.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127659623495766036/Antipasto-Salad-005.webp"
    )

    menuItem197 = MenuItem(
        itemName = "Grilled Chicken Club Sub",
        restaurantId = 22,
        price = 14.85,
        itemType = "Entree",
        description = "Mexican style crispy chicken sub with shaved onion, lettuce, and mayonnaise in our signature sub. With sweet teriyaki sauce.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496407402676254/subway_1.jpeg"
    )

    menuItem198 = MenuItem(
        itemName = "Grilled Cheesesteak Sub",
        restaurantId = 22,
        price = 14.85,
        itemType = "Entree",
        description = "Onions, green peppers, mushrooms, ketchup, mayo, and cheese in our signature buns.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127655945024065597/POTBELLY_SANDWICH1.jpeg"
    )

    menuItem199 = MenuItem(
        itemName = "Chocolate Chip Cookie",
        restaurantId = 22,
        price = 4.59,
        itemType = "Dessert",
        description = "Made fresh in house everyday!",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496801138770030/Single-Serve-Chocolate-Chip-Cookie-5-735x1103.webp"
    )


    menuItem200 = MenuItem(
        itemName = "Coke",
        restaurantId = 22,
        price = 4.59,
        itemType = "Drink",
        description = "20 oz. Bottle",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem201 = MenuItem(
        itemName = "Bottled Water",
        restaurantId = 22,
        price = 3.19,
        itemType = "Drink",
        description = "25 oz. Bottle",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )


    menuItem202 = MenuItem(
        itemName = "Avocado Eggrolls",
        restaurantId = 23,
        price = 17.95,
        itemType = "Side",
        description = "Avocado, Sun-Dried Tomato, Red Onion and Cilantro Fried in a Crisp Wrapper. Served with a Tamarind-Cashew Dipping Sauce",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665146110672948/avocado_eggrolls.jpeg"
    )

    menuItem203 = MenuItem(
        itemName = "Fried Calamari",
        restaurantId = 23,
        price = 18.50,
        itemType = "Side",
        description = "Fried Light and Crisp. Served with Garlic Dip and Cocktail Sauce",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665146366537919/download.jpeg"
    )

    menuItem204 = MenuItem(
        itemName = "Pepperoni Flatbread",
        restaurantId = 23,
        price = 12.95,
        itemType = "Entree",
        description = "Loaded with pepperoni, parmesan cheese, and house tomato sauce",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665676170043472/kids-pepperoni-flatbread.jpg"
    )

    menuItem205 = MenuItem(
        itemName = "Pasta Carbonara",
        restaurantId = 23,
        price = 17.95,
        itemType = "Entree",
        description = "Spaghetti with Smoked Bacon, Green Peas and a Garlic-Parmesan Cream Sauce",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665675880644689/carbonara.jpeg"
    )

    menuItem206 = MenuItem(
        itemName = "Oreo® Dream Extreme Cheesecake",
        restaurantId = 23,
        price = 11.95,
        itemType = "Dessert",
        description = "Creamy Cheesecake Layered with Oreo® Cookies, Topped with Oreo® Cookie Mousse and Chocolate Icing",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665146915979386/oreo_cheesecake.jpeg"
    )

    menuItem207 = MenuItem(
        itemName = "Caramel Apple Cheesecake",
        restaurantId = 23,
        price = 11.95,
        itemType = "Dessert",
        description = "Our Creamy Original Cheesecake Loaded with Caramel Apples, Topped with More Caramel on a Graham Crust",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665146630783109/cheesecake.jpeg"
    )


    menuItem208 = MenuItem(
        itemName = "Coke",
        restaurantId = 23,
        price = 4.59,
        itemType = "Drink",
        description = "20 oz. Bottle",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem209 = MenuItem(
        itemName = "Oreo® Milkshake",
        restaurantId = 23,
        price = 11.50,
        itemType = "Drink",
        description = "Oreo® Cookies Blended with Vanilla Ice Cream",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127657505305133137/oreo_cookie_shake.jpeg"
    )


    menuItem210 = MenuItem(
        itemName = "French Fries",
        restaurantId = 24,
        price = 9.95,
        itemType = "Side",
        description = "French fries fried in beef tallow.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127669070318292992/bbq_french_fries.jpeg"
    )

    menuItem211 = MenuItem(
        itemName = "Jumbo Chicken Strips",
        restaurantId = 24,
        price = 11.75,
        itemType = "Side",
        description = "3 pieces of fried chicken strips with cole slaw",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127669069932404746/bbq_chicken_strips.jpeg"
    )

    menuItem212 = MenuItem(
        itemName = "Pork Spare Ribs",
        restaurantId = 24,
        price = 12.95,
        itemType = "Entree",
        description = "Comes with pickles, sliced sweet Vidalia onion, and white bread. One rack is approximately 3 pounds.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127669782532075661/bbq_pork_ribs.jpeg"
    )

    menuItem213 = MenuItem(
        itemName = "0.5 lb Brisket",
        restaurantId = 24,
        price = 23.95,
        itemType = "Entree",
        description = "Comes with pickles, sliced sweet Vidalia onion, and white bread.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127669782192332981/bbq_brisket.jpeg"
    )

    menuItem214 = MenuItem(
        itemName = "Fresh Baked Chocolate Chip Cookie",
        restaurantId = 24,
        price = 4.00,
        itemType = "Dessert",
        description = "1 fresh baked chocolate chip cookie",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127496801138770030/Single-Serve-Chocolate-Chip-Cookie-5-735x1103.webp"
    )


    menuItem216 = MenuItem(
        itemName = "Coke",
        restaurantId = 24,
        price = 3.59,
        itemType = "Drink",
        description = "20 oz. Bottle",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem217 = MenuItem(
        itemName = "Bottled water",
        restaurantId = 24,
        price = 2.59,
        itemType = "Drink",
        description = "20 oz. Bottle",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem218 = MenuItem(
        itemName = "Mozzarella Sticks",
        restaurantId = 25,
        price = 15.99,
        itemType = "Side",
        description = "6 TGI Fridays mozzarella sticks with Asiago and Mozzarella cheese. Sprinkled with Parmesan-Romano. Served with marinara sauce.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127678714457628763/tgi_mozzarella.jpeg"
    )

    menuItem219 = MenuItem(
        itemName = "French Fries",
        restaurantId = 25,
        price = 2.59,
        itemType = "Side",
        description = "A classic everyone will love! Asiago cheese sprinkled on top",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127669070318292992/bbq_french_fries.jpeg"
    )

    menuItem220 = MenuItem(
        itemName = "Fridays Signature Whiskey-Glaze Burger",
        restaurantId = 25,
        price = 23.69,
        itemType = "Entree",
        description = "Burger with Signature Whiskey-Glaze, bacon, cheddar, lettuce, red onions, tomato and pickles.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127678715292299345/burger.jpeg"
    )

    menuItem221 = MenuItem(
        itemName = "Chicken Parmesan Pasta",
        restaurantId = 25,
        price = 25.79,
        itemType = "Entree",
        description = "Crispy chicken breast with marinara and cheese on fettuccine Alfredo. Topped with Parmesan crisps. Served with a warm garlic breadstick.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665675880644689/carbonara.jpeg"
    )

    menuItem265 = MenuItem(
        itemName = "Cinnabon Caramel Pecan Cheesecake",
        restaurantId = 25,
        price = 11.19,
        itemType = "Dessert",
        description = "Layers of Cinnabon cinnamon cheesecake and vanilla crunch cake topped with signature cream cheese frosting, caramel and glazed pecans. Served with vanilla bean ice cream.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665146630783109/cheesecake.jpeg"
    )

    menuItem266 = MenuItem(
        itemName = "Brownie Obsession",
        restaurantId = 25,
        price = 11.19,
        itemType = "Dessert",
        description = "A fudge brownie, vanilla bean ice cream, caramel sauce & glazed pecans",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127679612193873962/brownie_ice_cream.jpeg"
    )

    menuItem222 = MenuItem(
        itemName = "Coke (Bottle)",
        restaurantId = 25,
        price = 3.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem223 = MenuItem(
        itemName = "Bottled Water",
        restaurantId = 25,
        price = 2.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem224 = MenuItem(
        itemName = "House Salad",
        restaurantId = 26,
        price = 9.99,
        itemType = "Side",
        description = "Romaine, cucumber, tomato, and onions.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127659623848091808/caesar_salad.jpeg"
    )

    menuItem225 = MenuItem(
        itemName = "French Fries",
        restaurantId = 26,
        price = 7.59,
        itemType = "Side",
        description = "A classic everyone will love! Asiago cheese sprinkled on top",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127669070318292992/bbq_french_fries.jpeg"
    )

    menuItem226 = MenuItem(
        itemName = "Signature Burger",
        restaurantId = 26,
        price = 15.69,
        itemType = "Entree",
        description = "Burger with Signature sauce, bacon, cheddar, lettuce, red onions, tomato and pickles.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127678715292299345/burger.jpeg"
    )

    menuItem227 = MenuItem(
        itemName = "Big Breakfast Waffle",
        restaurantId = 26,
        price = 17.79,
        itemType = "Entree",
        description = "Crispy chicken breast with marinara and cheese on fettuccine Alfredo. Topped with Parmesan crisps. Served with a warm garlic breadstick.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127680910561652746/breakfast_waffle.jpeg"
    )

    menuItem228 = MenuItem(
        itemName = "Cheesecake",
        restaurantId = 26,
        price = 11.19,
        itemType = "Dessert",
        description = "Homemade cheesecake with signature cream cheese frosting and caramel.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665146630783109/cheesecake.jpeg"
    )

    menuItem229 = MenuItem(
        itemName = "Brownie Obsession",
        restaurantId = 27,
        price = 11.19,
        itemType = "Dessert",
        description = "A fudge brownie, vanilla bean ice cream, caramel sauce & glazed pecans",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127679612193873962/brownie_ice_cream.jpeg"
    )

    menuItem230 = MenuItem(
        itemName = "Oreo Milkshake",
        restaurantId = 26,
        price = 9.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127657505305133137/oreo_cookie_shake.jpeg"
    )

    menuItem231 = MenuItem(
        itemName = "Bottled Water",
        restaurantId = 26,
        price = 2.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem232 = MenuItem(
        itemName = "House Salad",
        restaurantId = 27,
        price = 14.99,
        itemType = "Side",
        description = "Romaine, cucumber, tomato, and onions.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127659623848091808/caesar_salad.jpeg"
    )

    menuItem233 = MenuItem(
        itemName = "Gold Coast Coconut Shrimp**",
        restaurantId = 27,
        price = 18.59,
        itemType = "Side",
        description = "Hand-dipped in batter, rolled in coconut and fried golden. Paired with Creole marmalade.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127682921428439230/coconut_shrimp.jpeg"
    )

    menuItem234 = MenuItem(
        itemName = "Bone-In Ribeye 18 oz.",
        restaurantId = 27,
        price = 37.39,
        itemType = "Entree",
        description = "Bone-in and extra marbled for maximum tenderness. Served with two freshly made sides.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127682921759776910/Ribeye_-_prime_bone--fd22f08262531494f30a804b8073c90e.jpg"
    )

    menuItem235 = MenuItem(
        itemName = "Filet® Mignon",
        restaurantId = 27,
        price = 35.79,
        itemType = "Entree",
        description = "The most tender and juicy thick cut seasoned and seared. Served with two freshly made sides.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127682921080295444/filet_mignon.jpeg"
    )

    menuItem236 = MenuItem(
        itemName = "Cheesecake",
        restaurantId = 27,
        price = 14.19,
        itemType = "Dessert",
        description = "Homemade cheesecake with signature cream cheese frosting and caramel.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127665146630783109/cheesecake.jpeg"
    )

    menuItem237 = MenuItem(
        itemName = "Tiramisu",
        restaurantId = 27,
        price = 15.19,
        itemType = "Dessert",
        description = "Coffee-flavoured Italian dessert made of ladyfingers dipped in coffee, layered with a whipped mixture of eggs, sugar, and mascarpone cheese, flavoured with cocoa.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127683779188764873/tiramisy.jpeg"
    )

    menuItem238 = MenuItem(
        itemName = "Oreo Milkshake",
        restaurantId = 27,
        price = 12.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127657505305133137/oreo_cookie_shake.jpeg"
    )

    menuItem239 = MenuItem(
        itemName = "Bottled Water",
        restaurantId = 27,
        price = 2.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )



    menuItem240 = MenuItem(
        itemName = "Steamed Dumplings",
        restaurantId = 28,
        price = 7.75,
        itemType = "Side",
        description = "6 pieces.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687979884871691/chinese_steamed_dumplings.jpeg"
    )

    menuItem241 = MenuItem(
        itemName = "Beef Teriyaki",
        restaurantId = 28,
        price = 8.59,
        itemType = "Side",
        description = "3 pieces.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687905578594345/chinese_beef_teriyaki.jpeg"
    )

    menuItem242 = MenuItem(
        itemName = " General Tso's Chicken",
        restaurantId = 28,
        price = 14.50,
        itemType = "Entree",
        description = "Served with roast pork fried rice and an egg roll.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687906639753407/chinese_general_tso.jpeg"
    )

    menuItem243 = MenuItem(
        itemName = "Beef with Broccoli",
        restaurantId = 28,
        price = 11.79,
        itemType = "Entree",
        description = "Served with white rice.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687905847017502/chinese_beef_with_broccoli.jpeg"
    )

    menuItem244 = MenuItem(
        itemName = "Sweet Red Bean Shortcake",
        restaurantId = 28,
        price = 5.00,
        itemType = "Dessert",
        description = "Homemade red bean shortcake.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687981243838504/chineses_shortcake.jpeg"
    )

    menuItem245 = MenuItem(
        itemName = "Pumpkin Cakes",
        restaurantId = 28,
        price = 7.99,
        itemType = "Dessert",
        description = "6 pieces",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687908023861259/chinese_pumpkin_cake.jpeg"
    )

    menuItem246 = MenuItem(
        itemName = "Coconut Milk",
        restaurantId = 28,
        price = 3.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687906383904888/chinese_coconut_drink.jpeg"
    )

    menuItem247 = MenuItem(
        itemName = "Plum Juice",
        restaurantId = 28,
        price = 4.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687907742855209/chinese_plum_juice.jpeg"
    )


    menuItem248 = MenuItem(
        itemName = " Wonton Soup",
        restaurantId = 29,
        price = 11.75,
        itemType = "Side",
        description = "Served with fried noodles. ",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687980551774258/chinese_wonton_soup.jpeg"
    )

    menuItem249 = MenuItem(
        itemName = "Beef Teriyaki",
        restaurantId = 29,
        price = 15.59,
        itemType = "Side",
        description = "3 pieces.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687905578594345/chinese_beef_teriyaki.jpeg"
    )

    menuItem250 = MenuItem(
        itemName = " General Tso's Chicken",
        restaurantId = 29,
        price = 33.50,
        itemType = "Entree",
        description = "Served with roast pork fried rice and an egg roll.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687906639753407/chinese_general_tso.jpeg"
    )

    menuItem251 = MenuItem(
        itemName = "Kung Pao Beef",
        restaurantId = 29,
        price = 32.79,
        itemType = "Entree",
        description = "Served with white rice.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687906895593572/chinese_kung_pao_beef.jpeg"
    )

    menuItem252 = MenuItem(
        itemName = "Mini Steamed White and Brown Buns",
        restaurantId = 29,
        price = 10.50,
        itemType = "Dessert",
        description = "6 pieces",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687979062800505/chinese_steamed_cake.jpeg"
    )

    menuItem253 = MenuItem(
        itemName = "Pumpkin Cakes",
        restaurantId = 29,
        price = 13.99,
        itemType = "Dessert",
        description = "6 pieces",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687908023861259/chinese_pumpkin_cake.jpeg"
    )

    menuItem254 = MenuItem(
        itemName = "Bottled water",
        restaurantId = 29,
        price = 3.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259766939689/water.webp"
    )

    menuItem255 = MenuItem(
        itemName = "Plum Juice",
        restaurantId = 29,
        price = 4.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687907742855209/chinese_plum_juice.jpeg"
    )




    menuItem256 = MenuItem(
        itemName = " Wonton Soup",
        restaurantId = 30,
        price = 9.50,
        itemType = "Side",
        description = "Served with fried noodles. ",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687980551774258/chinese_wonton_soup.jpeg"
    )

    menuItem257 = MenuItem(
        itemName = "Steamed Dumplings",
        restaurantId = 30,
        price = 11.59,
        itemType = "Side",
        description = "6 pieces.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687980551774258/chinese_wonton_soup.jpeg"
    )

    menuItem258 = MenuItem(
        itemName = "Sesame Chicken",
        restaurantId = 30,
        price = 18.50,
        itemType = "Entree",
        description = "Served with roast pork fried rice and an egg roll.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687978299433060/chinese_sesame_chicken.jpeg"
    )

    menuItem259 = MenuItem(
        itemName = "Kung Pao Beef",
        restaurantId = 30,
        price = 22.79,
        itemType = "Entree",
        description = "Served with white rice.",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687906895593572/chinese_kung_pao_beef.jpeg"
    )

    menuItem260 = MenuItem(
        itemName = "Mini Steamed White and Brown Buns",
        restaurantId = 30,
        price = 8.50,
        itemType = "Dessert",
        description = "6 pieces",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687979062800505/chinese_steamed_cake.jpeg"
    )

    menuItem261 = MenuItem(
        itemName = "Sweet Red Bean Pancake",
        restaurantId = 30,
        price = 10.99,
        itemType = "Dessert",
        description = "6 pieces",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687908346839070/chinese_red_bean_pancake.jpeg"
    )

    menuItem262 = MenuItem(
        itemName = "Coke Bottle",
        restaurantId = 30,
        price = 3.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127491259527872552/coca_cola.jpeg"
    )

    menuItem263 = MenuItem(
        itemName = "Plum Juice",
        restaurantId = 30,
        price = 4.99,
        itemType = "Drink",
        description = "",
        imageUrl = "https://cdn.discordapp.com/attachments/1116216556800716822/1127687907742855209/chinese_plum_juice.jpeg"
    )

    menu31item1 = MenuItem(
        itemName = "Sesame Chicken",
        restaurantId = 31,
        price = 15.95,
        itemType = "Entree",
        description = "Spicy. Served with steamed rice or fried rice.",
        imageUrl = "https://www.allrecipes.com/thmb/BRxk2aE9bO0vLDGTjIGx6FY5IkU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/141191-perfect-sesame-chicken-ddmfs-Beauty-1x2-1-d9ced248d1ee4c2788bbbc08514bf0ac.jpg"
    )

    menu31item2 = MenuItem(
            itemName = "Chicken Pad Thai",
            restaurantId = 31,
            price = 15.95,
            itemType = "Entree",
            description = "Spicy. Please note that noodle entrees (dinner size) are not served with rice.",
            imageUrl = "https://www.foodwinesunshine.com/wp-content/uploads/2015/08/chicken-pad-thai.jpg"
        )

    menu31item3 = MenuItem(
            itemName = "Crabmeat Cheese Wontons (6 pcs)",
            restaurantId = 31,
            price = 7.95,
            itemType = "Side",
            description = "Fresh, handmade wontons filled with imitation crab meat and cream cheese at the center, deep fried to a golden-brown color.",
            imageUrl = "https://dinnerthendessert.com/wp-content/uploads/2018/04/Crab-Rangoon-2-688x459.jpg"
        )

    menu31item4 = MenuItem(
            itemName = "Edamame",
            restaurantId = 31,
            price = 7.95,
            itemType = "Side",
            description = "Vegetarian.",
            imageUrl = "https://www.thespruceeats.com/thmb/R4Qmn_1AL_XYjGynPwtSoJCDavE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1-mixa-edamame-56a9bf613df78cf772aa2ced.jpg"
        )
    menu31item5 = MenuItem(
            itemName = "Capri Sun",
            restaurantId = 31,
            price = 1.50,
            itemType = "Drink",
            description = "",
            imageUrl = "https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/caprisun-wild-cherry-te-220815-7e2cd2.jpg"
        )
    menu31item6 = MenuItem(
            itemName = "Red Bull",
            restaurantId = 31,
            price = 2.99,
            itemType = "Drink",
            description = "",
            imageUrl = "https://vinepair.com/wp-content/uploads/2015/09/red-bull-card-375x450.jpg"
        )
    menu31item7 = MenuItem(
            itemName = "Fortune Cookies",
            restaurantId = 31,
            price = 0.50,
            itemType = "Dessert",
            description = "",
            imageUrl = "https://www.thespruceeats.com/thmb/tW07APdBu9qKH3MSKG4IVISfSzI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/fortune-cookie-recipe-694545-hero-01-3a76ceb6582e4893b49900785cd2333c.jpg"
        )


    menu32item1 = MenuItem(
            itemName = "Rigatoni Mangia Bene",
            restaurantId = 32,
            price = 17.95,
            itemType = "Entree",
            description = "Tube pasta, tomato cream sauce, grilled chicken, portobellos, garlic, Reggiano.",
            imageUrl = "https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1200,height=672,format=auto/https://doordash-static.s3.amazonaws.com/media/photos/70289ec4-5521-4655-ac3d-f37f5662e710-retina-large.jpg"
        )
    menu32item2 = MenuItem(
            itemName = "Panini Salsicca",
            restaurantId = 32,
            price = 16.95,
            itemType = "Entree",
            description = "Grilled sausage, roasted bell peppers, caramelized onions, basil, mozzarella cheese and marinara sauce.",
            imageUrl = "https://media-cdn.tripadvisor.com/media/photo-s/10/e3/8c/84/panino-con-salsiccia.jpg"
        )
    menu32item3 = MenuItem(
            itemName = "Chocolate Cake",
            restaurantId = 32,
            price = 9.95,
            itemType = "Dessert",
            description = "Moist chocolate cake made with sour cream and dark chocolate, rich pudding center, freshly whipped cream icing with a hint of grand Marnier.",
            imageUrl = "https://joyfoodsunshine.com/wp-content/uploads/2020/08/best-chocolate-cake-recipe-from-scratch-8.jpg"
        )
    menu32item4 = MenuItem(
            itemName = "Sicilian Cheesecake",
            restaurantId = 32,
            price = 9.95,
            itemType = "Dessert",
            description = "Cream cheese, pastry crust sprinkled with cinnamon. Sour cream glaze, topped with berries.",
            imageUrl = "https://ninakneadstobake.com/wp-content/uploads/2022/03/Olive-Garden-Sicilian-Cheesecake-500x375.jpg"
        )
    menu32item5 = MenuItem(
            itemName = "Dr. Pepper",
            restaurantId = 32,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://assets.turbologo.com/blog/en/2020/02/19084621/Dr.-pepper-can-958x575.png"
        )
    menu32item6 = MenuItem(
            itemName = "Arnold Palmer",
            restaurantId = 32,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://www.thespruceeats.com/thmb/bsrl2EqzsL9qv9kjpRUBAG_NRV0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/SES-arnold-palmer-mocktail-recipe-760357-hero-01-eeba74f983314829ab6e41918541abfc.jpg"
        )
    menu32item7 = MenuItem(
            itemName = "Italian Green Beans",
            restaurantId = 32,
            price = 4.35,
            itemType = "Side",
            description = "These Italian green beans are perfect with any meal.",
            imageUrl = "https://40aprons.com/wp-content/uploads/2021/09/italian-green-beans-6-500x500.jpg"
        )
    menu32item8 = MenuItem(
            itemName = "Edamame",
            restaurantId = 32,
            price = 7.95,
            itemType = "Side",
            description = "Vegetarian.",
            imageUrl = "https://www.thespruceeats.com/thmb/R4Qmn_1AL_XYjGynPwtSoJCDavE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1-mixa-edamame-56a9bf613df78cf772aa2ced.jpg"
        )


    menu33item1 = MenuItem(
            itemName = "Spaghetti and Meatballs",
            restaurantId = 33,
            price = 13.99,
            itemType = "Entree",
            description = "Includes house salad, garlic knots, and parmesan cheese.",
            imageUrl = "https://static.onecms.io/wp-content/uploads/sites/43/2022/04/07/21353-italian-spaghetti-sauce-with-meatballs-3x2-138.jpg"
        )
    menu33item2 = MenuItem(
            itemName = "Fettuccine Alfredo",
            restaurantId = 33,
            price = 13.99,
            itemType = "Entree",
            description = "A blend of fresh cream, butter, and parmesan cheese. Includes salad, ricotta cheese rolled in pasta and topped with melted mozzarella. Includes salad, garlic knots, and parmesan cheese.",
            imageUrl = "https://www.allrecipes.com/thmb/LjXULjH7Yd_BeLLTLOlyaDx-xzE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/19402-Quick-And-Easy-Alfredo-Sauce-mfs_002-df1c96e0f9514d2191d0d8ce4c8a9745.jpg"
        )
    menu33item3 = MenuItem(
            itemName = "Fried Calamari",
            restaurantId = 33,
            price = 10.99,
            itemType = "Side",
            description = "Fried calamari.",
            imageUrl = "https://lilsweetspiceadvice.com/wp-content/uploads/2020/11/Gluten-Free-Fried-Calamari-with-Sriracha-Lemon-Basil-Aioli-6-480x270.jpg"
        )
    menu33item4 = MenuItem(
            itemName = "Bruschetta",
            restaurantId = 33,
            price = 8.99,
            itemType = "Side",
            description = "Bruschetta.",
            imageUrl = "https://upload.wikimedia.org/wikipedia/commons/1/1f/2014_Bruschetta_The_Larder_Chiang_Mai.jpg"
        )
    menu33item5 = MenuItem(
            itemName = "Cannoli",
            restaurantId = 33,
            price = 3.99,
            itemType = "Dessert",
            description = "Cannoli.",
            imageUrl = "https://images-gmi-pmc.edge-generalmills.com/771be6a6-f5d9-4c36-9480-e2f08b7fe6eb.jpg"
        )
    menu33item6 = MenuItem(
            itemName = "Homemade NY Style Cheesecake",
            restaurantId = 33,
            price = 4.50,
            itemType = "Dessert",
            description = "Homemade NY style cheesecake.",
            imageUrl = "https://images-gmi-pmc.edge-generalmills.com/493ba1aa-8d32-47e1-a6e3-399e159be720.jpg"
        )
    menu33item7 = MenuItem(
            itemName = "Dr. Pepper",
            restaurantId = 33,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://assets.turbologo.com/blog/en/2020/02/19084621/Dr.-pepper-can-958x575.png"
        )
    menu33item8 = MenuItem(
            itemName = "Sprite",
            restaurantId = 33,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://sushieki.ca/wp-content/uploads/2022/05/6000200192740_600x600.jpg"
        )



    menu34item1 = MenuItem(
            itemName = "Sakura Roll",
            restaurantId = 34,
            price = 15.95,
            itemType = "Entree",
            description = "Inside: Avocado and spicy tuna. Topped: Salmon, tuna, and roast garlic. Comes with cucumber.",
            imageUrl = "https://i.pinimg.com/originals/e7/46/18/e7461883e7a1bd849c0680a246986eab.jpg"
        )
    menu34item2 = MenuItem(
            itemName = "Mexican Roll",
            restaurantId = 34,
            price = 15.95,
            itemType = "Entree",
            description = "Inside: Spicy crabmeat and spicy shrimp. Topped: Avocado and jalapeno. Rolls come with cucumber.",
            imageUrl = "https://thefoodxp.com/wp-content/uploads/2020/09/Mexican-Sushi-1-e1599375403504.jpg"
        )
    menu34item3 = MenuItem(
            itemName = "Crispy Rice (3 pcs)",
            restaurantId = 34,
            price = 11.95,
            itemType = "Side",
            description = "Crispy rice.",
            imageUrl = "https://www.bhg.com/thmb/GGbLGk52369Z1sWXyLCbGiubYu0=/6000x0/filters:no_upscale():strip_icc()/BHG-Crispy-Rice-Sushi-Bites-5CVUpf-qqbcA_QHYeSbGhJ-f475fca42dc344d5897f698cbe719757.jpg"
        )
    menu34item4 = MenuItem(
            itemName = "Garlic Edamame",
            restaurantId = 34,
            price = 9.95,
            itemType = "Side",
            description = "Garlic flavored edamame.",
            imageUrl = "https://www.thespruceeats.com/thmb/R4Qmn_1AL_XYjGynPwtSoJCDavE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1-mixa-edamame-56a9bf613df78cf772aa2ced.jpg"
        )
    menu34item5 = MenuItem(
            itemName = "Mochi",
            restaurantId = 34,
            price = 8.95,
            itemType = "Dessert",
            description = "Mango, green tea, strawberry, vanilla, and chocolate.",
            imageUrl = "https://images-gmi-pmc.edge-generalmills.com/771be6a6-f5d9-4c36-9480-e2f08b7fe6eb.jpg"
        )
    menu34item6 = MenuItem(
            itemName = "Tempura Ice Cream",
            restaurantId = 34,
            price = 9.95,
            itemType = "Dessert",
            description = "Green tea and vanilla",
            imageUrl = "https://media-cdn.tripadvisor.com/media/photo-s/13/20/e7/0b/deep-fried-vanilla-tempura.jpg"
        )
    menu34item7 = MenuItem(
            itemName = "Dr. Pepper",
            restaurantId = 34,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://assets.turbologo.com/blog/en/2020/02/19084621/Dr.-pepper-can-958x575.png"
        )
    menu34item8 = MenuItem(
            itemName = "Sprite",
            restaurantId = 34,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://sushieki.ca/wp-content/uploads/2022/05/6000200192740_600x600.jpg"
        )



    menu35item1 = MenuItem(
            itemName = "Spider Roll",
            restaurantId = 35,
            price = 10.00,
            itemType = "Entree",
            description = "Deep-fried soft shell crab, avocado, cucumber, and unagi sauce.",
            imageUrl = "https://ichisushi.com/wp-content/uploads/2022/04/Best-Spider-Roll-Sushi-Recipes-to-Give-a-Try.jpg"
        )
    menu35item2 = MenuItem(
            itemName = "Night Fighter Roll",
            restaurantId = 35,
            price = 15.00,
            itemType = "Entree",
            description = "In: shrimp tempura, cucumber, and cream cheese. Top: unagi, avocado, spicy mayonnaise, and unagi sauce.",
            imageUrl = "https://www.sushigardenaptos.com/wp-content/uploads/2020/09/night-fighter-1.jpg"
        )
    menu35item3 = MenuItem(
            itemName = "Miso Soup",
            restaurantId = 35,
            price = 2.00,
            itemType = "Side",
            description = "Miso soup.",
            imageUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Miso_Soup_001.jpg/1200px-Miso_Soup_001.jpg"
        )
    menu35item4 = MenuItem(
            itemName = "Garlic Edamame",
            restaurantId = 35,
            price = 9.95,
            itemType = "Side",
            description = "Garlic flavored edamame.",
            imageUrl = "https://www.thespruceeats.com/thmb/R4Qmn_1AL_XYjGynPwtSoJCDavE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1-mixa-edamame-56a9bf613df78cf772aa2ced.jpg"
        )
    menu35item5 = MenuItem(
            itemName = "Mochi",
            restaurantId = 35,
            price = 8.95,
            itemType = "Dessert",
            description = "Mango, green tea, strawberry, vanilla, and chocolate.",
            imageUrl = "https://images-gmi-pmc.edge-generalmills.com/771be6a6-f5d9-4c36-9480-e2f08b7fe6eb.jpg"
        )
    menu35item6 = MenuItem(
            itemName = "Tempura Ice Cream",
            restaurantId = 35,
            price = 9.95,
            itemType = "Dessert",
            description = "Green tea and vanilla",
            imageUrl = "https://media-cdn.tripadvisor.com/media/photo-s/13/20/e7/0b/deep-fried-vanilla-tempura.jpg"
        )
    menu35item7 = MenuItem(
            itemName = "Ramune Japanese Soda",
            restaurantId = 35,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://i5.peapod.com/c/7N/7N4FS.jpg"
        )
    menu35item8 = MenuItem(
            itemName = "Soda",
            restaurantId = 35,
            price = 2.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://sushieki.ca/wp-content/uploads/2022/05/6000200192740_600x600.jpg"
        )




    menu36item1 = MenuItem(
            itemName = "911 Roll",
            restaurantId = 36,
            price = 16.99,
            itemType = "Entree",
            description = "Inside: spicy tuna and cucumber. Outside: avocado, spicy mayonnaise, eel sauce, and spicy sauce.",
            imageUrl = "https://sushidamu.com/wp-content/uploads/2020/10/911.jpg"
        )
    menu36item2 = MenuItem(
            itemName = "Washington Roll",
            restaurantId = 36,
            price = 16.99,
            itemType = "Entree",
            description = "Inside: crabmeat and cucumber. Outside: salmon with spicy mayonnaise, eel sauce, and green onion.",
            imageUrl = "https://media-cdn.tripadvisor.com/media/photo-s/03/ac/e6/b4/washington-roll-eel-roll.jpg"
        )
    menu36item3 = MenuItem(
            itemName = "Miso Soup",
            restaurantId = 36,
            price = 4.99,
            itemType = "Side",
            description = "Miso soup.",
            imageUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Miso_Soup_001.jpg/1200px-Miso_Soup_001.jpg"
        )
    menu36item4 = MenuItem(
            itemName = "Garlic Edamame",
            restaurantId = 36,
            price = 9.95,
            itemType = "Side",
            description = "Garlic flavored edamame.",
            imageUrl = "https://www.thespruceeats.com/thmb/R4Qmn_1AL_XYjGynPwtSoJCDavE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1-mixa-edamame-56a9bf613df78cf772aa2ced.jpg"
        )
    menu36item5 = MenuItem(
            itemName = "Mochi",
            restaurantId = 36,
            price = 8.95,
            itemType = "Dessert",
            description = "Mango, green tea, strawberry, vanilla, and chocolate.",
            imageUrl = "https://images-gmi-pmc.edge-generalmills.com/771be6a6-f5d9-4c36-9480-e2f08b7fe6eb.jpg"
        )
    menu36item6 = MenuItem(
            itemName = "Tempura Ice Cream",
            restaurantId = 36,
            price = 9.95,
            itemType = "Dessert",
            description = "Green tea and vanilla",
            imageUrl = "https://media-cdn.tripadvisor.com/media/photo-s/13/20/e7/0b/deep-fried-vanilla-tempura.jpg"
        )
    menu36item7 = MenuItem(
            itemName = "Ramune Japanese Soda",
            restaurantId = 36,
            price = 4.00,
            itemType = "Drink",
            description = "",
            imageUrl = "https://i5.peapod.com/c/7N/7N4FS.jpg"
        )
    menu36item8 = MenuItem(
            itemName = "Fountain Soda",
            restaurantId = 36,
            price = 3.49,
            itemType = "Drink",
            description = "",
            imageUrl = "https://sushieki.ca/wp-content/uploads/2022/05/6000200192740_600x600.jpg"
        )


    menu37item1 = MenuItem(
            itemName = "Garlic Butter Shrimp & Pork Belly",
            restaurantId = 37,
            price = 15.45,
            itemType = "Entree",
            description = "Perfectly seasoned and pan seared garlic butter shrimp, tender chunks of our slow braised pork belly. Choose your base, toppings, optional add-ons, and sauces.",
            imageUrl = "https://popmenucloud.com/cdn-cgi/image/width%3D1920%2Cheight%3D1920%2Cfit%3Dscale-down%2Cformat%3Dauto%2Cquality%3D60/qvioyhnc/c8fef2d7-0e99-4d1c-ba5a-40a35f627468.jpg"
        )
    menu37item2 = MenuItem(
            itemName = "Cosmic Roll",
            restaurantId = 37,
            price = 10.95,
            itemType = "Entree",
            description = "Hearty and deliciously fresh spring roll sandwich wrap filled with grilled chicken, noodles, veggies and fillings.",
            imageUrl = "https://popmenucloud.com/cdn-cgi/image/width%3D1920%2Cheight%3D1920%2Cfit%3Dscale-down%2Cformat%3Dauto%2Cquality%3D60/qvioyhnc/f5b32bfe-c330-44bc-baeb-fe48b54b87c8.jpg"
        )
    menu37item3 = MenuItem(
            itemName = "Garlic Edamame",
            restaurantId = 36,
            price = 9.95,
            itemType = "Side",
            description = "Garlic flavored edamame.",
            imageUrl = "https://www.thespruceeats.com/thmb/R4Qmn_1AL_XYjGynPwtSoJCDavE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/1-mixa-edamame-56a9bf613df78cf772aa2ced.jpg"
        )
    menu37item4 = MenuItem(
            itemName = "Onion RIngs",
            restaurantId = 37,
            price = 8.95,
            itemType = "Side",
            description = "Beer battered onion rings, crispy golden brown with your choice of 2 sauces.",
            imageUrl = "https://natashaskitchen.com/wp-content/uploads/2022/06/Onion-Rings-Recipe-SQ.jpg"
        )
    menu37item5 = MenuItem(
            itemName = "Mochi",
            restaurantId = 37,
            price = 8.95,
            itemType = "Dessert",
            description = "Mango, green tea, strawberry, vanilla, and chocolate.",
            imageUrl = "https://images-gmi-pmc.edge-generalmills.com/771be6a6-f5d9-4c36-9480-e2f08b7fe6eb.jpg"
        )
    menu37item6 = MenuItem(
            itemName = "Tempura Ice Cream",
            restaurantId = 37,
            price = 9.95,
            itemType = "Dessert",
            description = "Green tea and vanilla",
            imageUrl = "https://media-cdn.tripadvisor.com/media/photo-s/13/20/e7/0b/deep-fried-vanilla-tempura.jpg"
        )
    menu37item7 = MenuItem(
            itemName = "Fountain Soda",
            restaurantId = 37,
            price = 3.49,
            itemType = "Drink",
            description = "",
            imageUrl = "https://sushieki.ca/wp-content/uploads/2022/05/6000200192740_600x600.jpg"
        )



    menu38item1 = MenuItem(
            itemName = "Garlic Butter Shrimp & Beef Short Rib",
            restaurantId = 38,
            price = 16.95,
            itemType = "Entree",
            description = "Garlic butter shrimp and grilled beef short rib with your choice of base, toppings, optional add-ons, and sauces.",
            imageUrl = "https://popmenucloud.com/cdn-cgi/image/width%3D1920%2Cheight%3D1920%2Cfit%3Dscale-down%2Cformat%3Dauto%2Cquality%3D60/qvioyhnc/a80e0a5c-13ef-4f49-9c19-f1cbd1d5b82f.jpg"
        )
    menu38item2 = MenuItem(
            itemName = "Grilled Chicken Bowl",
            restaurantId = 38,
            price = 14.95,
            itemType = "Entree",
            description = "A customer favorite! Tender chunks of boneless and skinless grilled chicken, with olive oil and seasonings. Choose your base, toppings, optional add-ons, and sauces on the side.",
            imageUrl = "https://popmenucloud.com/cdn-cgi/image/width%3D1920%2Cheight%3D1920%2Cfit%3Dscale-down%2Cformat%3Dauto%2Cquality%3D60/qvioyhnc/46c7e7ac-eb64-4ad4-b21a-556e69261a70.jpg"
        )
    menu38item3 = MenuItem(
            itemName = "Umami Fries",
            restaurantId = 38,
            price = 8.95,
            itemType = "Side",
            description = "Crispy hot fries tossed with our own Chili Chop sauce and topped with furikake seasoning.",
            imageUrl = "https://magazine.foodpanda.my/wp-content/uploads/sites/12/2020/04/cropped-Umami-Fries.jpeg"
        )
    menu38item4 = MenuItem(
            itemName = "Onion RIngs",
            restaurantId = 38,
            price = 8.95,
            itemType = "Side",
            description = "Beer battered onion rings, crispy golden brown with your choice of 2 sauces.",
            imageUrl = "https://natashaskitchen.com/wp-content/uploads/2022/06/Onion-Rings-Recipe-SQ.jpg"
        )
    menu38item5 = MenuItem(
            itemName = "Chocolate Cake",
            restaurantId = 38,
            price = 9.95,
            itemType = "Dessert",
            description = "Moist chocolate cake made with sour cream and dark chocolate, rich pudding center, freshly whipped cream icing with a hint of grand Marnier.",
            imageUrl = "https://joyfoodsunshine.com/wp-content/uploads/2020/08/best-chocolate-cake-recipe-from-scratch-8.jpg"
        )
    menu38item6 = MenuItem(
            itemName = "Tempura Ice Cream",
            restaurantId = 38,
            price = 9.95,
            itemType = "Dessert",
            description = "Green tea and vanilla",
            imageUrl = "https://media-cdn.tripadvisor.com/media/photo-s/13/20/e7/0b/deep-fried-vanilla-tempura.jpg"
        )
    menu38item7 = MenuItem(
            itemName = "Fountain Soda",
            restaurantId = 38,
            price = 3.49,
            itemType = "Drink",
            description = "",
            imageUrl = "https://sushieki.ca/wp-content/uploads/2022/05/6000200192740_600x600.jpg"
        )
    menu38item8 = MenuItem(
            itemName = "Capri Sun",
            restaurantId = 38,
            price = 1.50,
            itemType = "Drink",
            description = "",
            imageUrl = "https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/caprisun-wild-cherry-te-220815-7e2cd2.jpg"
        )



    menu39item1 = MenuItem(
            itemName = "Omelette Platter",
            restaurantId = 39,
            price = 15.95,
            itemType = "Entree",
            description = "Many omelettes.",
            imageUrl = "https://freshfusion.ca/wp-content/uploads/2021/05/Omlette-Platter-e1621882933123.jpg"
        )
    menu39item2 = MenuItem(
            itemName = "Grilled Chicken Bowl",
            restaurantId = 39,
            price = 18.99,
            itemType = "Entree",
            description = "Complete meal packs, individually bagged and labelled.",
            imageUrl = "https://freshfusion.ca/wp-content/uploads/2021/05/BoxedLunch.jpg"
        )
    menu39item3 = MenuItem(
            itemName = "Cheese Platter",
            restaurantId = 39,
            price = 7.99,
            itemType = "Side",
            description = "Cheese platter.",
            imageUrl = "https://freshfusion.ca/wp-content/uploads/2020/12/Cheese-Platter-1.jpg"
        )
    menu39item4 = MenuItem(
            itemName = "Fruit Platter",
            restaurantId = 39,
            price = 5.99,
            itemType = "Side",
            description = "Fruit platter.",
            imageUrl = "https://freshfusion.ca/wp-content/uploads/2014/10/fruitscat-1.jpg"
        )
    menu39item5 = MenuItem(
            itemName = "Vanilla Swirl Pastry",
            restaurantId = 39,
            price = 27.99,
            itemType = "Dessert",
            description = "Vanilla swirl pastries.",
            imageUrl = "https://freshfusion.ca/wp-content/uploads/2021/05/vanilla-swirls-e1621881361817.jpeg"
        )
    menu39item6 = MenuItem(
            itemName = "Chocolate Chunk Brownie",
            restaurantId = 39,
            price = 27.99,
            itemType = "Dessert",
            description = "Chocolate chunk brownies",
            imageUrl = "https://freshfusion.ca/wp-content/uploads/2021/05/Chewy-Chocolate-Chunk-Brownie-2.jpg"
        )
    menu39item7 = MenuItem(
            itemName = "Nestea Iced Tea 500ml",
            restaurantId = 39,
            price = 2.79,
            itemType = "Drink",
            description = "",
            imageUrl = "https://freshfusion.ca/wp-content/uploads/2022/09/ice-tea.webp"
        )
    menu39item8 = MenuItem(
            itemName = "Coke Zero Can 355ml",
            restaurantId = 39,
            price = 1.99,
            itemType = "Drink",
            description = "",
            imageUrl = "https://post.healthline.com/wp-content/uploads/2019/08/is-coke-zero-bad-for-you-1200x628-facebook.jpg"
        )


# db.session.add(menuItem1)
# db.session.add(menuItem2)
# db.session.add(menuItem3)
# db.session.add(menuItem4)
# db.session.add(menuItem5)
# db.session.add(menuItem6)
# db.session.add(menuItem7)
# db.session.add(menuItem8)
# db.session.add(menuItem9)
# db.session.add(menuItem10)
# db.session.add(menuItem11)
# db.session.commit()


    menu_items = [
        menuItem1,
        menuItem2,
        menuItem3,
        menuItem4,
        menuItem5,
        menuItem6,
        menuItem7,
        menuItem8,
        menuItem9,
        menuItem10,
        menuItem11,
        menuItem12,
        menuItem13,
        menuItem14,
        menuItem15,
        menuItem16,
        menuItem17,
        menuItem18,
        menuItem19,
        menuItem20,
        menuItem21,
        menuItem22,
        menuItem23,
        menuItem24,
        menuItem25,
        menuItem26,
        menuItem27,
        menuItem28,
        menuItem29,
        menuItem30,
        menuItem31,
        menuItem32,
        menuItem33,
        menuItem34,
        menuItem35,
        menuItem36,
        menuItem37,
        menuItem38,
        menuItem39,
        menuItem40,
        menuItem41,
        menuItem42,
        menuItem43,
        menuItem44,
        menuItem45,
        menuItem46,
        menuItem47,
        menuItem48,
        menuItem49,
        menuItem50,
        menuItem51,
        menuItem52,
        menuItem53,
        menuItem54,
        menuItem55,
        menuItem56,
        menuItem57,
        menuItem58,
        menuItem59,
        menuItem60,
        menuItem61,
        menuItem62,
        menuItem63,
        menuItem64,
        menuItem65,
        menuItem66,
        menuItem67,
        menuItem68,
        menuItem69,
        menuItem70,
        menuItem71,
        menuItem72,
        menuItem73,
        menuItem74,
        menuItem75,
        menuItem76,
        menuItem77,
        menuItem78,
        menuItem79,
        menuItem80,
        menuItem81,
        menuItem82,
        menuItem83,
        menuItem84,
        menuItem85,
        menuItem86,
        menuItem87,
        menuItem88,
        menuItem89,
        menuItem90,
        menuItem91,
        menuItem92,
        menuItem93,
        menuItem94,
        menuItem95,
        menuItem96,
        menuItem97,
        menuItem98,
        menuItem99,
        menuItem100,
        menuItem101,
        menuItem102,
        menuItem103,
        menuItem104,
        menuItem105,
        menuItem106,
        menuItem107,
        menuItem108,
        menuItem109,
        menuItem110,
        menuItem111,
        menuItem112,
        menuItem113,
        menuItem114,
        menuItem115,
        menuItem116,
        menuItem117,
        menuItem118,
        menuItem119,
        menuItem120,
        menuItem121,
        menuItem151,
        menuItem152,
        menuItem153,
        menuItem154,
        menuItem155,
        menuItem156,
        menuItem157,
        menuItem158,
        menuItem159,
        menuItem160,
        menuItem161,
        menuItem162,
        menuItem163,
        menuItem164,
        menuItem165,
        menuItem166,
        menuItem167,
        menuItem168,
        menuItem169,
        menuItem170,
        menuItem171,
        menuItem172,
        menuItem173,
        menuItem174,
        menuItem175,
        menuItem176,
        menuItem177,
        menuItem178,
        menuItem179,
        menuItem180,
        menuItem181,
        menuItem182,
        menuItem183,
        menuItem184,
        menuItem185,
        menuItem186,
        menuItem187,
        menuItem188,
        menuItem189,
        menuItem190,
        menuItem191,
        menuItem192,
        menuItem193,
        menuItem194,
        menuItem195,
        menuItem196,
        menuItem197,
        menuItem198,
        menuItem199,
        menuItem200,
        menuItem201,
        menuItem202,
        menuItem203,
        menuItem204,
        menuItem205,
        menuItem206,
        menuItem207,
        menuItem208,
        menuItem209,
        menuItem210,
        menuItem211,
        menuItem212,
        menuItem213,
        menuItem214,
        menuItem216,
        menuItem217,
        menuItem218,
        menuItem219,
        menuItem220,
        menuItem221,
        menuItem222,
        menuItem223,
        menuItem224,
        menuItem225,
        menuItem226,
        menuItem227,
        menuItem228,
        menuItem229,
        menuItem230,
        menuItem231,
        menuItem232,
        menuItem233,
        menuItem234,
        menuItem235,
        menuItem236,
        menuItem237,
        menuItem238,
        menuItem239,
        menuItem240,
        menuItem241,
        menuItem242,
        menuItem243,
        menuItem244,
        menuItem245,
        menuItem246,
        menuItem247,
        menuItem248,
        menuItem249,
        menuItem250,
        menuItem251,
        menuItem252,
        menuItem253,
        menuItem254,
        menuItem255,
        menuItem256,
        menuItem257,
        menuItem258,
        menuItem259,
        menuItem260,
        menuItem261,
        menuItem262,
        menuItem263,
        menuItem264,
        menuItem265,

        menu31item1,
        menu31item2,
        menu31item3,
        menu31item4,
        menu31item5,
        menu31item6,
        menu31item7,

        menu32item1,
        menu32item2,
        menu32item3,
        menu32item4,
        menu32item5,
        menu32item6,
        menu32item7,
        menu32item8,

        menu33item1,
        menu33item2,
        menu33item3,
        menu33item4,
        menu33item5,
        menu33item6,
        menu33item7,
        menu33item8,

        menu34item1,
        menu34item2,
        menu34item3,
        menu34item4,
        menu34item5,
        menu34item6,
        menu34item7,
        menu34item8,

        menu35item1,
        menu35item2,
        menu35item3,
        menu35item4,
        menu35item5,
        menu35item6,
        menu35item7,
        menu35item8,

        menu36item1,
        menu36item2,
        menu36item3,
        menu36item4,
        menu36item5,
        menu36item6,
        menu36item7,
        menu36item8,

        menu37item1,
        menu37item2,
        menu37item3,
        menu37item4,
        menu37item5,
        menu37item6,
        menu37item7,

        menu38item1,
        menu38item2,
        menu38item3,
        menu38item4,
        menu38item5,
        menu38item6,
        menu38item7,
        menu38item8,

        menu39item1,
        menu39item2,
        menu39item3,
        menu39item4,
        menu39item5,
        menu39item6,
        menu39item7,
        menu39item8
    ]
    for menu_item in menu_items:
        db.session.add(menu_item)
    db.session.commit()

def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menuitems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menuitems"))

    db.session.commit()
