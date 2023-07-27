from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    reviews = [
        Review(
            restaurantId = 2,
            userId = 2,
            rating = 5,
            description = "Absolutely phenomenal! The food was a culinary delight, with each dish bursting with exquisite flavors. The service was impeccable, with attentive staff going above and beyond to ensure a memorable dining experience. Highly recommended!"
        ),

        Review(
            restaurantId = 4,
            userId = 2,
            rating = 5,
            description = "Absolutely phenomenal! The food was a culinary delight, with each dish bursting with exquisite flavors. The service was impeccable, with attentive staff going above and beyond to ensure a memorable dining experience. Highly recommended!"
        ),

        Review(
            restaurantId = 1,
            userId = 3,
            rating = 5,
            description="Fast and convenient! The Big Mac and fries arrived hot and were satisfying."
        ),

        Review(
            restaurantId = 3,
            userId = 2,
            rating = 5,
            description = "Great place for a casual meal! The food was delicious and reasonably priced. The atmosphere was relaxed and inviting, perfect for catching up with friends or enjoying a laid-back evening. I'll definitely be coming back!"
        ),

        Review(
            restaurantId = 1,
            userId = 1,
            rating=5,
            description="Decent fast food option. The McNuggets were okay, but the order was missing ketchup."
        ),
        Review(
            restaurantId=1,
            userId=4,
            rating=5,
            description="Always a reliable choice! The Quarter Pounder and McFlurry were tasty as usual."
        ),
        Review(
            restaurantId=1,
            userId=5,
            rating=4,
            description="Great for a quick meal! The Happy Meal and apple slices were perfect for the kids."
            ),
        Review(
            restaurantId=1,
            userId=6,
            rating=5,
            description="Always a delightful experience at McDonald's! The menu has something for everyone, and the staff is friendly and efficient."
            ) ,
        Review(
            restaurantId=1,
            userId=7,
            rating=3,
            description="Not impressed with the quality of food. The burgers were greasy, and the fries were overcooked. Disappointing visit overall."
            ),
        Review(
            restaurantId=1,
            userId=8,
            rating=4,
            description="Good fast food joint with a variety of options. The service was quick, and the restaurant was clean and tidy."
            ),
        Review(
            restaurantId=1,
            userId=9,
            rating=4,
            description="Decent food, but the place was crowded and noisy during peak hours. It's better to visit during off-peak times."
            ),
        Review(
            restaurantId=1,
            userId=10,
            rating=5,
            description="Loved the new menu additions! The McChicken sandwich was fantastic, and the McFlurry is a must-try dessert."
            ),
        Review(
            restaurantId=1,
            userId=11,
            rating=2,
            description="Horrible experience! The order was messed up, and the staff was unapologetic. Avoid this McDonald's location!"
            ),

        Review(
            restaurantId=2,
            userId=4,
            rating=4,
            description="Delicious Chinese cuisine! The Kung Pao Chicken and Mongolian Beef were flavorful and perfectly cooked."
            ),
        Review(
            restaurantId=2,
            userId=5,
            rating=5,
            description="PF Chang's never disappoints! The service was exceptional, and the Orange Chicken was a delightful blend of sweet and tangy."
        ),
        Review(
            restaurantId=2,
            userId=6,
            rating=3,
            description="Average experience. The food was alright, but nothing stood out as exceptional."
        ),
        Review(
            restaurantId=2,
            userId=7,
            rating=5,
            description="Authentic flavors and excellent service! The Dynamite Shrimp and Dan Dan Noodles were top-notch."
        ),
        Review(
            restaurantId=2,
            userId=8,
            rating=3,
            description="Not impressed with the quality of food. The dishes were too greasy for my liking."
        ),
        Review(
            restaurantId=2,
            userId=9,
            rating=4,
            description="Great ambiance and a diverse menu! The lettuce wraps were a fantastic appetizer, and the portion sizes were generous."
        ),
        Review(
            restaurantId=2,
            userId=10,
            rating=5,
            description="Highly recommended! The Crispy Honey Chicken and Shrimp Dumplings were exquisite."
        ),
        Review(
            restaurantId=2,
            userId=11,
            rating=3,
            description="Terrible service! The staff was rude and inattentive, and the food took forever to arrive."
        ),
        Review(
            restaurantId=2,
            userId=12,
            rating=4,
            description="Delightful dining experience! The Walnut Shrimp and Singapore Street Noodles were my favorites."
        ),
        Review(
            restaurantId=2,
            userId=13,
            rating=3,
            description="Decent Chinese food, but a bit overpriced compared to other local options."
        ),

        Review(
            restaurantId=3,
            userId=1,
            rating=4,
            description="Delicious Italian dishes delivered right on time! The pizza was hot and perfectly cooked, and the pasta was flavorful."
        ),
        Review(
            restaurantId=3,
            userId=5,
            rating=5,
            description="Outstanding delivery service! The food arrived piping hot, and the Tiramisu dessert was a delightful treat."
        ),
        Review(
            restaurantId=3,
            userId=6,
            rating=3,
            description="Average delivery experience. The food was decent, but the delivery took longer than expected."
        ),
        Review(
            restaurantId=3,
            userId=7,
            rating=5,
            description="Fantastic food and quick delivery! The Chicken Alfredo and Garlic Bread were simply amazing."
        ),
        Review(
            restaurantId=3,
            userId=8,
            rating=3,
            description="Disappointing delivery service. The food arrived cold, and it seemed like the order was mishandled during delivery."
        ),
        Review(
            restaurantId=3,
            userId=9,
            rating=5,
            description="Great Italian feast delivered to my doorstep! The Margherita pizza and Calzone were scrumptious."
        ),
        Review(
            restaurantId=3,
            userId=10,
            rating=5,
            description="Highly satisfied with the delivery and food quality! The Lasagna and Cannoli were outstanding."
        ),
        Review(
            restaurantId=3,
            userId=11,
            rating=3,
            description="Horrible delivery experience! The food was late, and the delivery driver was rude."
        ),
        Review(
            restaurantId=3,
            userId=12,
            rating=4,
            description="Delightful Italian cuisine delivered with care! The Ravioli and Caesar Salad were delightful."
        ),
        Review(
            restaurantId=3,
            userId=13,
            rating=3,
            description="The food was okay, but the delivery took longer than expected, and the packaging could be improved."
        ),

         Review(
            restaurantId=4,
            userId=13,
            rating=5,
            description="Amazing Mexican food delivered right to my doorstep! The tacos and guacamole were full of flavor."
        ),
        Review(
            restaurantId=4,
            userId=10,
            rating=4,
            description="Great delivery service and tasty dishes! The Quesadillas and Salsa Verde were delicious."
        ),
        Review(
            restaurantId=4,
            userId=2,
            rating=4,
            description="Decent food, but the delivery was a bit slow. The Burritos and Chips were alright."
        ),
        Review(
            restaurantId=4,
            userId=5,
            rating=5,
            description="Authentic Mexican flavors! The Enchiladas and Mexican Rice were a hit."
        ),
        Review(
            restaurantId=4,
            userId=6,
            rating=3,
            description="Disappointed with the delivery experience. The food arrived cold, and the order was incomplete."
        ),
        Review(
            restaurantId=4,
            userId=7,
            rating=4,
            description="Delicious Mexican feast delivered with care! The Tamales and Guava Margarita were fantastic."
        ),
        Review(
            restaurantId=4,
            userId=8,
            rating=5,
            description="Highly recommended! The Fajitas and Churros were delightful."
        ),
        Review(
            restaurantId=4,
            userId=9,
            rating=1,
            description="Terrible delivery service! The food was delayed, and the delivery driver was unapologetic."
        ),
        
        Review(
            restaurantId=5,
            userId=1,
            rating=5,
            description="Absolutely love Chick-fil-A! Their chicken sandwiches and waffle fries are always a treat."
        ),
        Review(
            restaurantId=5,
            userId=3,
            rating=4,
            description="Delicious fast food! The nuggets and Chick-fil-A sauce are my go-to favorites."
        ),
        Review(
            restaurantId=5,
            userId=4,
            rating=3,
            description="Average experience. The service was quick, but the chicken sandwich was a bit greasy."
        ),
        Review(
            restaurantId=5,
            userId=5,
            rating=5,
            description="Outstanding customer service! The employees are always friendly and helpful."
        ),
        Review(
            restaurantId=5,
            userId=6,
            rating=3,
            description="Disappointed with the quality. The food seemed overcooked and lacked flavor."
        ),
        Review(
            restaurantId=5,
            userId=7,
            rating=4,
            description="Tasty chicken and great service! The Chick-n-Strips and lemonade were refreshing."
        ),
        Review(
            restaurantId=5,
            userId=8,
            rating=5,
            description="Highly satisfied with my order! The chicken sandwich and milkshake were delightful."
        ),
        Review(
            restaurantId=5,
            userId=9,
            rating=4,
            description="Decent fast-food option, but nothing extraordinary."
        ),

        Review(
            restaurantId=6,
            userId=1,
            rating=4,
            description="Taco Bell never disappoints! The Crunchwrap Supreme and Doritos Locos Tacos are my favorites."
        ),
        Review(
            restaurantId=6,
            userId=3,
            rating=5,
            description="Delicious fast food! The Quesarito and Cinnamon Twists are must-try items."
        ),
        Review(
            restaurantId=6,
            userId=4,
            rating=3,
            description="Average experience. The food was alright, but the drive-thru line was quite long."
        ),
        Review(
            restaurantId=6,
            userId=5,
            rating=5,
            description="Quick and tasty! The Cheesy Gordita Crunch and Baja Blast Freeze were a perfect combo."
        ),
        Review(
            restaurantId=6,
            userId=6,
            rating=2,
            description="Disappointed with the quality. The food seemed cold and lacked the usual flavors."
        ),
        Review(
            restaurantId=6,
            userId=7,
            rating=4,
            description="Great value for money! The Nacho Fries and Beefy 5-Layer Burrito were satisfying."
        ),
        Review(
            restaurantId=6,
            userId=8,
            rating=5,
            description="Highly satisfied with my order! The Chalupa Supreme and Mexican Pizza were fantastic."
        ),
        Review(
            restaurantId=6,
            userId=9,
            rating=3,
            description="Decent fast-food option, but the wait time was longer than expected."
        ),
        Review(
            restaurantId=7,
            userId=3,
            rating=4,
            description="Enjoyed the burgers! The patties were juicy, and the toppings were fresh."
        ),
        Review(
            restaurantId=7,
            userId=4,
            rating=5,
            description="Best burger joint in town! The fries were crispy, and the milkshakes were creamy."
        ),
        Review(
            restaurantId=8,
            userId=5,
            rating=3,
            description="Decent burger place. The burgers were tasty, but the service was slow."
        ),
        Review(
            restaurantId=8,
            userId=6,
            rating=4,
            description="Good variety of burgers! The veggie burger and sweet potato fries were excellent."
        ),
        Review(
            restaurantId=9,
            userId=7,
            rating=2,
            description="Not impressed with the Mexican food. The tacos were bland, and the guacamole lacked flavor."
        ),
        Review(
            restaurantId=9,
            userId=8,
            rating=1,
            description="Awful experience! The service was terrible, and the food was not authentic Mexican cuisine."
        ),

        Review(
            restaurantId=10,
            userId=9,
            rating=4,
            description="Delicious Mexican dishes! The enchiladas and salsa were a hit."
        ),
        Review(
            restaurantId=10,
            userId=10,
            rating=5,
            description="Authentic Mexican flavors! The quesadillas and churros were heavenly."
        ),
          Review(
            restaurantId=11,
            userId=4,
            rating=3,
            description="Decent burger place. The burgers were tasty, but the service was slow."
        ),
        Review(
            restaurantId=11,
            userId=10,
            rating=4,
            description="Good variety of burgers! The veggie burger and sweet potato fries were excellent."
        ),
        Review(
            restaurantId=12,
            userId=12,
            rating=4,
            description="Delicious Mexican dishes! The enchiladas and salsa were a hit."
        ),
        Review(
            restaurantId=12,
            userId=1,
            rating=5,
            description="Authentic Mexican flavors! The quesadillas and churros were heavenly."
        ),

        Review(
            restaurantId=19, 
            userId=1,
            rating=4,
            description="Great selection of Subway Clubs! The turkey club with avocado and bacon was my favorite."
        ),
        Review(
            restaurantId=19, 
            userId=4,
            rating=3,
            description="Average experience. The bread was a bit soggy, but the fresh veggies made up for it."
        ),
        Review(
            restaurantId=19,  
            userId=12,
            rating=5,
            description="Love the variety of Subway Clubs! The Italian B.M.T. club with extra cheese was fantastic."
        ),
        Review(
            restaurantId=19,  
            userId=14,
            rating=5,
            description="Absolutely delicious! The Steak & Cheese club with all the toppings was a mouthwatering delight."
        ),

         Review(
            restaurantId=20, 
            userId=1,
            rating=4,
            description="Great selection of Subway Clubs! The turkey club with avocado and bacon was my favorite."
        ),
        Review(
            restaurantId=20, 
            userId=4,
            rating=3,
            description="Average experience. The bread was a bit soggy, but the fresh veggies made up for it."
        ),
        Review(
            restaurantId=20,  
            userId=13,
            rating=5,
            description="Love the variety of Subway Clubs! The Italian B.M.T. club with extra cheese was fantastic."
        ),
        Review(
            restaurantId=20,  
            userId=11,
            rating=5,
            description="Absolutely delicious! The Steak & Cheese club with all the toppings was a mouthwatering delight."
        ),

        Review(
            restaurantId=16,
            userId=1,
            rating=4,
            description="Delicious pizza selection! The pepperoni pizza was perfectly cheesy and had a thin crust."
        ),
        Review(
            restaurantId=16,
            userId=11,
            rating=5,
            description="Best pizza in town! The Margherita pizza with fresh basil was a delight."
        ),
        Review(
            restaurantId=16,
            userId=5,
            rating=4,
            description="Great pizza place! The BBQ Chicken pizza and garlic breadsticks were mouthwatering."
        ),
        Review(
            restaurantId=16,
            userId=10,
            rating=3,
            description="Decent pizza experience. The pizza had a good amount of toppings, but the delivery was a bit late."
        ),

        Review(
            restaurantId=17,
            userId=6,
            rating=3,
            description="Decent pizza place. The toppings were good, but the pizza crust was a bit too thick for my liking."
        ),
        Review(
            restaurantId=17,
            userId=7,
            rating=4,
            description="Tasty pizza options! The Meat Lovers pizza and garlic knots were a delicious combo."
        ),
        Review(
            restaurantId=17,
            userId=8,
            rating=5,
            description="Fantastic pizza joint! The Veggie Supreme pizza with a crispy crust was superb."
        ),
        Review(
            restaurantId=17,
            userId=9,
            rating=2,
            description="Not impressed with the pizza quality. The pizza sauce was too tangy for my taste."
        ),
        Review(
            restaurantId=18,
            userId=10,
            rating=2,
            description="Disappointed with the pizza quality. The pizza was overcooked and lacked flavor."
        ),
        Review(
            restaurantId=18,
            userId=1,
            rating=1,
            description="Terrible pizza experience! The delivery was late, and the pizza was cold."
        ),
        Review(
            restaurantId=18,
            userId=6,
            rating=4,
            description="Great pizza delivery! The Pepperoni and Mushroom pizza was delicious and arrived on time."
        ),
        Review(
            restaurantId=18,
            userId=13,
            rating=5,
            description="Outstanding pizza options! The Buffalo Chicken pizza and cheesy breadsticks were amazing."
        ),
        Review(
            restaurantId=13,
            userId=1,
            rating=4,
            description="Delicious Asian cuisine! The sushi rolls and miso soup were delightful."
        ),
        Review(
            restaurantId=13,
            userId=5,
            rating=5,
            description="Authentic Japanese flavors! The teriyaki chicken and tempura were a perfect combo."
        ),
        Review(
            restaurantId=13,
            userId=6,
            rating=4,
            description="Great service and tasty dishes! The Pad Thai and spring rolls were fantastic."
        ),
        Review(
            restaurantId=13,
            userId=7,
            rating=3,
            description="Decent Asian restaurant. The dumplings were good, but the portion size was small."
        ),
        Review(
            restaurantId=15,
            userId=8,
            rating=5,
            description="Amazing Thai food! The Green Curry and Mango Sticky Rice were heavenly."
        ),
        Review(
            restaurantId=15,
            userId=9,
            rating=4,
            description="Delicious Vietnamese dishes! The pho and fresh spring rolls were excellent."
        ),
        Review(
            restaurantId=15,
            userId=10,
            rating=3,
            description="Average experience. The service was slow, and the food lacked some authenticity."
        ),
        Review(
            restaurantId=15,
            userId=11,
            rating=5,
            description="Outstanding Chinese cuisine! The Kung Pao Chicken and Szechuan noodles were flavorful."
        ),
        Review(
            restaurantId=34,
            userId=12,
            rating=4,
            description="Great Korean BBQ! The marinated beef and kimchi were a tasty combination."
        ),
        Review(
            restaurantId=34,
            userId=13,
            rating=5,
            description="Excellent service and authentic Korean flavors! The bibimbap and banchan were delicious."
        ),
        Review(
            restaurantId=34,
            userId=1,
            rating=3,
            description="Decent Korean restaurant. The side dishes were good, but the main course was mediocre."
        ),
        Review(
            restaurantId=34,
            userId=5,
            rating=4,
            description="Tasty hot pot experience! The spicy broth and assorted ingredients were delightful."
        ),
        Review(
            restaurantId=35,
            userId=6,
            rating=4,
            description="Enjoyable Japanese teppanyaki! The hibachi show and steak were impressive."
        ),
        Review(
            restaurantId=35,
            userId=7,
            rating=5,
            description="Highly recommended sushi spot! The Dragon Roll and Volcano Roll were fantastic."
        ),
        Review(
            restaurantId=35,
            userId=8,
            rating=3,
            description="Average dining experience. The sushi rolls were decent, but the service could be improved."
        ),
        Review(
            restaurantId=35,
            userId=9,
            rating=4,
            description="Good Thai cuisine! The red curry and coconut milk soup were flavorful."
        ),

        Review(
            restaurantId=37,
            userId=4,
            rating=4,
            description="Great options for healthy eaters! The avocado toast and green smoothie were delicious."
        ),
        Review(
            restaurantId=37,
            userId=5,
            rating=5,
            description="Fresh and flavorful salads! The Cobb Salad and Balsamic Vinaigrette were amazing."
        ),
        Review(
            restaurantId=37,
            userId=6,
            rating=4,
            description="Tasty vegan dishes! The Beyond Burger and sweet potato fries were delightful."
        ),
        Review(
            restaurantId=37,
            userId=7,
            rating=3,
            description="Decent selection of healthy food. The quinoa bowl was good, but the portion size was small."
        ),

        # RestaurantId 38 (Healthy Food Restaurant)
        Review(
            restaurantId=38,
            userId=8,
            rating=5,
            description="Highly recommended for health-conscious eaters! The acai bowl and fresh fruit platter were outstanding."
        ),
        Review(
            restaurantId=38,
            userId=9,
            rating=4,
            description="Nutritious and delicious! The grilled chicken salad and lemon herb dressing were fantastic."
        ),
        Review(
            restaurantId=38,
            userId=10,
            rating=3,
            description="Average experience. The smoothie bowl was alright, but it lacked some variety."
        ),
        Review(
            restaurantId=38,
            userId=11,
            rating=5,
            description="Fantastic vegetarian options! The falafel wrap and tahini sauce were scrumptious."
        ),
        Review(
            restaurantId=39,
            userId=12,
            rating=4,
            description="Great place for healthy sandwiches! The turkey avocado wrap and mixed greens were satisfying."
        ),
        Review(
            restaurantId=39,
            userId=13,
            rating=5,
            description="Excellent gluten-free choices! The quinoa salad and gluten-free brownie were delightful."
        ),
        Review(
            restaurantId=39,
            userId=4,
            rating=3,
            description="Decent organic menu. The vegetable soup was good, but the service was a bit slow."
        ),
        Review(
            restaurantId=39,
            userId=1,
            rating=4,
            description="Tasty and nutritious bowls! The poke bowl and fresh ingredients were delicious."
        ),
        Review(
            restaurantId=32,
            userId=4,
            rating=4,
            description="Delicious Italian dishes! The pasta carbonara and garlic bread were fantastic."
        ),
        Review(
            restaurantId=32,
            userId=5,
            rating=5,
            description="Authentic Italian flavors! The Margherita pizza and tiramisu were superb."
        ),
        Review(
            restaurantId=32,
            userId=6,
            rating=4,
            description="Great service and tasty pasta! The Bolognese and lasagna were delightful."
        ),
        Review(
            restaurantId=32,
            userId=7,
            rating=3,
            description="Decent Italian restaurant. The portion size of the pasta dishes could be larger."
        ),
        Review(
            restaurantId=33,
            userId=8,
            rating=5,
            description="Amazing Italian cuisine! The pesto gnocchi and garlic knots were heavenly."
        ),
        Review(
            restaurantId=33,
            userId=1,
            rating=4,
            description="Delicious risotto and bruschetta! The flavors were authentic and well-balanced."
        ),
        Review(
            restaurantId=33,
            userId=10,
            rating=3,
            description="Average Italian experience. The pizza was decent, but it could have been more flavorful."
        ),
        Review(
            restaurantId=33,
            userId=11,
            rating=5,
            description="Outstanding Italian dishes! The seafood linguine and tiramisu were top-notch."
        ),

        Review(
            restaurantId=23,
            userId=4,
            rating=5,
            description="A must-visit for cheesecake lovers! The Oreo Dream Extreme Cheesecake was heavenly."
        ),
        Review(
            restaurantId=23,
            userId=5,
            rating=4,
            description="Great food and wide menu selection! The Chicken Madeira and Avocado Eggrolls were fantastic."
        ),
        Review(
            restaurantId=23,
            userId=6,
            rating=3,
            description="Average dining experience. The portions were generous, but the service could have been better."
        ),
        Review(
            restaurantId=23,
            userId=7,
            rating=5,
            description="Outstanding desserts! The Godiva Chocolate Cheesecake and Red Velvet Cheesecake were divine."
        ),
        Review(
            restaurantId=28,
            userId=4,
            rating=4,
            description="Delicious Chinese dishes! The General Tso's Chicken and spring rolls were fantastic."
        ),
        Review(
            restaurantId=28,
            userId=1,
            rating=5,
            description="Authentic Chinese flavors! The Kung Pao Shrimp and fried rice were superb."
        ),
        Review(
            restaurantId=28,
            userId=6,
            rating=4,
            description="Great service and tasty dim sum! The dumplings and buns were delightful."
        ),
        Review(
            restaurantId=28,
            userId=7,
            rating=3,
            description="Decent Chinese restaurant. The portion size of the entrees could be larger."
        ),

        Review(
            restaurantId=29,
            userId=8,
            rating=5,
            description="Amazing Szechuan cuisine! The Mapo Tofu and Dan Dan Noodles were heavenly."
        ),
        Review(
            restaurantId=29,
            userId=9,
            rating=4,
            description="Delicious hot pot! The spicy broth and meat selection were excellent."
        ),
        Review(
            restaurantId=29,
            userId=10,
            rating=3,
            description="Average Chinese experience. The service was slow, but the food was decent."
        ),
        Review(
            restaurantId=29,
            userId=11,
            rating=5,
            description="Outstanding Peking Duck! The dish was carved at the table and tasted incredible."
        ),

        # RestaurantId 30 (Chinese Restaurant)
        Review(
            restaurantId=30,
            userId=12,
            rating=4,
            description="Great place for Cantonese cuisine! The Dim Sum and BBQ Pork were tasty."
        ),
        Review(
            restaurantId=30,
            userId=13,
            rating=5,
            description="Excellent Chinese hot pot! The ingredients were fresh, and the broth was flavorful."
        ),
        Review(
            restaurantId=30,
            userId=4,
            rating=3,
            description="Decent Chinese restaurant. The stir-fried noodles were good, but the service could be improved."
        ),
        Review(
            restaurantId=30,
            userId=5,
            rating=4,
            description="Tasty Shanghai dumplings! The soup dumplings and pot stickers were delicious."
        ),

        Review(
            restaurantId=31,
            userId=1,
            rating=4,
            description="Enjoyable Chinese hot pot! The variety of dipping sauces and meat options were great."
        ),
        Review(
            restaurantId=31,
            userId=7,
            rating=5,
            description="Highly recommended Szechuan restaurant! The spicy Mapo Tofu and dry-fried green beans were fantastic."
        ),
        Review(
            restaurantId=31,
            userId=8,
            rating=3,
            description="Average dining experience. The orange chicken was alright, but it could have been more flavorful."
        ),
        Review(
            restaurantId=31,
            userId=9,
            rating=4,
            description="Good Chinese cuisine! The General Tso's Tofu and broccoli stir-fry were flavorful."
        ),

        Review(
            restaurantId=7, 
            userId=4,
            rating=5,
            description="Delicious and juicy burgers! The patties were perfectly cooked and the toppings were fresh."
        ),
        Review(
            restaurantId=7,  
            userId=5,
            rating=4,
            description="Great fast food spot for burgers! The fries were crispy and the shakes were creamy and flavorful."
        ),

        Review(
            restaurantId=7, 
            userId=6,
            rating=5,
            description="Best burgers in town! The buns were fresh, and the special sauce added the perfect touch of flavor."
        ),
           Review(
            restaurantId=8,
            userId=4,
            rating=5,
            description="Delicious and juicy burgers! The patties were perfectly cooked and the toppings were fresh."
        ),
        Review(
            restaurantId=8,  
            userId=5,
            rating=4,
            description="Great fast food spot for burgers! The fries were crispy and the shakes were creamy and flavorful."
        ),
        Review(
            restaurantId=8, 
            userId=6,
            rating=5,
            description="Best burgers in town! The buns were fresh, and the special sauce added the perfect touch of flavor."
        ),
          Review(
            restaurantId=5,
            userId=3,
            rating=5,
            description="Love Chick-fil-A! The chicken sandwich and waffle fries are always top-notch."
        ),
        Review(
            restaurantId=5,
            userId=9,
            rating=4,
            description="Great customer service and delicious food! The lemonade and nuggets are my favorites."
        ),
        Review(
            restaurantId=5,
            userId=10,
            rating=4,
            description="Solid fast food choice! The Chick-fil-A sauce and friendly staff make every visit enjoyable."
        ),
          Review(
            restaurantId=9,
            userId=8,
            rating=5,
            description="Authentic Mexican flavors! The quesadillas and churros were heavenly."
        ),
          Review(
            restaurantId=10,
            userId=13,
            rating=5,
            description="Authentic Mexican flavors! Fast delivery."
        ),
        Review(
            restaurantId=12,
            userId=8,
            rating=5,
            description="Authentic Mexican flavors! The tacos and guacamole were absolutely delicious."
        ),
        Review(
            restaurantId=12,
            userId=9,
            rating=4,
            description="Great ambiance and friendly staff! The enchiladas and margaritas were a hit."
        ),
        Review(
            restaurantId=12,
            userId=10,
            rating=3,
            description="Decent Mexican restaurant. The service was a bit slow, but the fajitas were tasty."
        ),
        Review(
            restaurantId=27,
            userId=1,
            rating=5,
            description="Amazing steakhouse experience! The ribeye steak and loaded baked potato were exceptional."
        ),
        Review(
            restaurantId=27,
            userId=9,
            rating=4,
            description="Great quality steaks and fast delivery! The New York strip and creamed spinach were delicious."
        ),
        Review(
            restaurantId=27,
            userId=10,
            rating=5,
            description="Best steak in town! The filet mignon and sautéed mushrooms were melt-in-your-mouth tender."
        ),
        Review(
            restaurantId=27,
            userId=11,
            rating=3,
            description="Decent steakhouse. The service was average, but the ribeye steak was good."
        ),
        Review(
            restaurantId=27,
            userId=12,
            rating=4,
            description="Tasty and satisfying steaks! The porterhouse and garlic butter were excellent."
        ),
        Review(
            restaurantId=25,
            userId=8,
            rating=4,
            description="Good comfort food! The loaded potato skins and buffalo wings were enjoyable."
        ),
        Review(
            restaurantId=25,
            userId=9,
            rating=3,
            description="Decent takeout experience. The burgers were alright, but the service was slow."
        ),
        Review(
            restaurantId=25,
            userId=10,
            rating=5,
            description="Great value and tasty food! The mozzarella sticks and Jack Daniel's ribs were fantastic."
        ),
        Review(
            restaurantId=25,
            userId=1,
            rating=4,
            description="Satisfying meals and friendly staff! The crispy chicken sandwich and fries were delicious."
        ),
        Review(
            restaurantId=25,
            userId=12,
            rating=5,
            description="Always reliable for a quick bite! The loaded potato skins and nachos were on point."
        ),
                Review(
            restaurantId=24,
            userId=8,
            rating=5,
            description="The best BBQ in town! The smoked brisket and mac n' cheese were heavenly."
        ),
        Review(
            restaurantId=24,
            userId=1,
            rating=4,
            description="Delicious BBQ! The pulled pork sandwich and coleslaw were a perfect combo."
        ),
        Review(
            restaurantId=24,
            userId=10,
            rating=3,
            description="Average BBQ experience. The ribs were decent, but the BBQ sauce was too tangy."
        ),
        Review(
            restaurantId=24,
            userId=11,
            rating=5,
            description="Outstanding BBQ joint! The ribs and baked beans were finger-licking good."
        ),
        Review(
            restaurantId=24,
            userId=12,
            rating=4,
            description="Great for BBQ lovers! The smoked chicken and cornbread were flavorful."
        ),
        Review(
            restaurantId=21,
            userId=8,
            rating=4,
            description="Delicious sandwiches! The club sandwich and sweet potato fries were a hit."
        ),
        Review(
            restaurantId=21,
            userId=1,
            rating=3,
            description="Decent lunch spot. The turkey club was good, but the service was a bit slow."
        ),
        Review(
            restaurantId=21,
            userId=10,
            rating=5,
            description="Great variety and quick pickup! The BLT and coleslaw were satisfying."
        ),
        Review(
            restaurantId=21,
            userId=11,
            rating=4,
            description="Fresh ingredients and tasty sandwiches! The chicken avocado club was flavorful."
        ),
        Review(
            restaurantId=21,
            userId=12,
            rating=5,
            description="Always my go-to for sandwiches! The Reuben and pickle spear were delicious."
        ),

        Review(
            restaurantId=22,
            userId=8,
            rating=4,
            description="Delicious sandwiches! The club sandwich and sweet potato fries were a hit."
        ),
        Review(
            restaurantId=22,
            userId=9,
            rating=3,
            description="Decent lunch spot. The turkey club was good, but the service was a bit slow."
        ),
        Review(
            restaurantId=22,
            userId=10,
            rating=5,
            description="Great variety and quick pickup! The BLT and coleslaw were satisfying."
        ),
        Review(
            restaurantId=22,
            userId=11,
            rating=4,
            description="Fresh ingredients and tasty sandwiches! The chicken avocado club was flavorful."
        ),
        Review(
            restaurantId=22,
            userId=12,
            rating=5,
            description="Always my go-to for sandwiches! The Reuben and pickle spear were delicious."
        ),
        Review(
            restaurantId=11,
            userId=8,
            rating=5,
            description="In-N-Out never disappoints! The Double-Double and animal-style fries were mouthwatering."
        ),
        Review(
            restaurantId=11,
            userId=9,
            rating=4,
            description="Great burgers and quick service! The secret menu options and shakes were delightful."
        ),
        Review(
            restaurantId=11,
            userId=10,
            rating=3,
            description="Decent fast food experience. The burger patties were thin, but the ingredients tasted fresh."
        )






    ]


    # db.session.add(review1)
    # db.session.add(review2)
    # db.session.add(review3)
    # db.session.add(review4)
    # db.session.add(review5)
    db.session.add_all(reviews)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()  
