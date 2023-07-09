from app.models import db, MenuItem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_menu_items():

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
        menuItem265
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

