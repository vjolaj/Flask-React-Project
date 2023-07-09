# seed restaurants
from app.models import db, Restaurant, environment, SCHEMA
from sqlalchemy.sql import text
def seed_restaurants():
    restaurant1 = Restaurant(
        ownerId = 1,
        name = "Mcdonalds",
        address = "234 Drive",
        cuisineType= "FastFood",
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
        imageUrl = "https://content.pymnts.com/wp-content/uploads/2020/02/PF-Changs-Food-Delivery-Apps.jpg",
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
        name = "Chick-fill-A",
        address = "234 Scenic Gulf",
        cuisineType = "FastFood",
        priceRange = "$",
        imageUrl = "https://tb-static.uber.com/prod/image-proc/processed_images/14aecf3db7eea1dd2fe67a004a272ae2/3ac2b39ad528f8c8c5dc77c59abb683d.jpeg",
        description = "Chick-fil-A is an American fast food restaurant chain and the largest chain specializing in chicken sandwiches."
    )

    restaurant6 = Restaurant(
        ownerId = 2,
        name = "Taco Bell",
        address = "786 5th Ave",
        cuisineType = "FastFood",
        priceRange = "$",
        imageUrl = "https://tb-static.uber.com/prod/image-proc/processed_images/dee68afc57b7e5967d7aec211bb4effa/3ac2b39ad528f8c8c5dc77c59abb683d.jpeg",
        description = "Taco Bell is a subsidiary of Yum!"
    )

    restaurant7 = Restaurant(
        ownerId = 3,
        name = "Five Guys",
        address = "673 Ocean Drive",
        cuisineType = "FastFood",
        priceRange = "$",
        imageUrl = "https://www.brightonmarina.co.uk/wp-content/uploads/2020/11/FG-generic-web.png",
        description = "American fast food chain focused on hamburgers, hot dogs, and french fries."
    )

    restaurant8 = Restaurant(
        ownerId = 2,
        name = "Shake Shack",
        address = "786 6th Avenue",
        cuisineType = "FastFood",
        priceRange = "$$",
        imageUrl = "https://www.tastingtable.com/img/gallery/free-shake-shack-postmates-delivery/image-import.jpg",
        description = "Shake Shack is an American fast casual restaurant chain based in New York City."
    )


    restaurant9 = Restaurant(
        ownerId = 2,
        name = "El Sol Mexicano",
        address = "123 Main Street",
        cuisineType = "Mexican",
        priceRange = "$$",
        imageUrl = "https://duyt4h9nfnj50.cloudfront.net/resized/16f61060f98ded0e3991ebeae0225766-w2880-dc.jpg",
        description = "El Sol Mexicano is a vibrant Mexican restaurant located in the heart of the city."
    )

    restaurant10 = Restaurant(
        ownerId = 3,
        name = "La Cantina Mexicana",
        address = "456 Maple Avenue",
        cuisineType = "Mexican",
        priceRange = "$",
        imageUrl = "https://d1ralsognjng37.cloudfront.net/9ba8dac9-f3d0-4de0-92e1-f9331f040936",
        description = "Experience the true taste of Mexico at La Cantina Mexicana. From mouthwatering tacos to zesty guacamole."
    )   

    restaurant11 = Restaurant(
        ownerId = 3,
        name = "In-N-Out Burger",
        address = "672 Ocean Drive",
        cuisineType = "FastFood",
        priceRange = "$",
        imageUrl = "https://whatnowphoenix.com/wp-content/uploads/sites/7/2023/01/In-N-Out-Burger-Files-Proposal-With-the-City-of-Mesa.jpg",
        description = "In-N-Out Burger is an American regional chain of fast food restaurants with locations primarily in California"
    )

    restaurant12 = Restaurant(
        ownerId=2,
        name="Pepitos",
        address="123 Main Street",
        cuisineType="Mexican",
        priceRange="$$$$",
        imageUrl = "https://duyt4h9nfnj50.cloudfront.net/resized/d1772bc1acf58b56d18ca48c9ec15c3f-w2880-b4.jpg",
        description="El Sol Mexicano is a vibrant Mexican restaurant located in the heart of the city."
    )


    restaurant13 = Restaurant(
        ownerId=2,
        name="Sakura Sushi Bar",
        address="456 Elm Street",
        cuisineType="Asian",
        priceRange="$$$",
        imageUrl = "https://res.cloudinary.com/tf-lab/image/upload/f_auto,q_auto,w_480,h_270/restaurant/7aae154e-be0b-467b-bee2-2a1db9de7cd1/c0768c5c-826f-4652-b41e-6c83908d8487.jpg",
        description="Sakura Sushi Bar offers an extensive selection of fresh and delicious sushi rolls, sashimi, and Japanese specialties."
    )


    restaurant14 = Restaurant(
        ownerId=2,
        name="Ming's Chinese Restaurant",
        address="123 Main Street",
        cuisineType="Asian",
        priceRange="$",
        imageUrl = "https://www.whitsundaymenu.com.au/wp-content/uploads/2022/05/alley-cat-may-2022-31.jpg",
        description="Ming's Chinese Restaurant offers a wide range of traditional Chinese dishes, including savory stir-fries, flavorful noodles, and delicious dim sum."
    )


    restaurant15 = Restaurant(
        ownerId=2,
        name="Taste of Asia",
        address="789 Pine Street",
        cuisineType="Asian",
        priceRange="$$",
        imageUrl = "https://media1.agfg.com.au/images/listing/74539/hero-400.jpg",
        description="Taste of India brings the rich and diverse flavors of Indian cuisine to your table."
    )

    restaurant16 = Restaurant(
        ownerId = 3,
        name = "Pizza Hut",
        address = "432 5th Avenue",
        cuisineType = "Pizza",
        priceRange = "$",
        imageUrl = "https://tb-static.uber.com/prod/image-proc/processed_images/928567ed0e575277315d1929edc427bc/132976946f0604ab7f405a880c4eb56e.jpeg",
        description = "Best American Pizza"
    )

    restaurant17 = Restaurant(
        ownerId = 2,
        name = "Papa John's",
        address = "256 Ocean Drive",
        cuisineType = "Pizza",
        priceRange = "$$",
        imageUrl = "https://www.papajohns.com/crispy-parm-pizza/img/crispy-parm-hero.jpg",
        description = "Best American Pizza"
    )

    restaurant18 = Restaurant(
        ownerId = 2,
        name = "Grimaldis",
        address = "563 56th Street",
        cuisineType = "Pizza",
        priceRange = "$$$",
        imageUrl = "https://townsquare.media/site/675/files/2023/01/attachment-grimaldis.jpg?w=980&q=75",
        description = "Casual, Brooklyn-based pizzeria chain serving brick-oven pies & calzones, plus wine & beer."
    )

    restaurant19 = Restaurant(
        ownerId = 2,
        name = "Subway",
        address = "432 Main Ave",
        cuisineType = "Sandwich",
        priceRange = "$",
        imageUrl = "https://imageproxy.wolt.com/venue/6049c80b5e17b192228d7c27/8b14dbba-965d-11ed-81ff-22360be22887_8717d940_7231_11ed_8e97_26dde300d060_wolt_cover_1440x810px.jpg",
        description = "American multinational fast food restaurant franchise that specializes in submarine sandwiches, wraps, salads and drinks"
    )

    restaurant20 = Restaurant(
        ownerId=2,
        name="Jimmy John's",
        address="123 Main Street",
        cuisineType="Sandwich",
        priceRange="$$",
        imageUrl="https://d1ralsognjng37.cloudfront.net/2b5027ab-2f8e-4a04-8240-2aa9a48150cc.jpeg",
        description="The Sandwich Spot offers a variety of freshly made sandwiches with high-quality ingredients."
    )

    restaurant21 = Restaurant(
        ownerId=2,
        name="Potbelly Sandwich Works",
        address="30 Rockefeller Plaza Ste L3",
        cuisineType="Sandwich",
        priceRange="$",
        imageUrl="https://cdn.discordapp.com/attachments/1116216556800716822/1127654941239037992/potbelly.jpeg",
        description="Retro-style counter-serve chain known for made-to-order toasted sandwiches, salads & baked goods."
    )


    restaurant22 = Restaurant(
        ownerId = 3,
        name = "Sub Cult",
        address = "652 5th Av",
        cuisineType = "Sandwich",
        priceRange = "$$$",
        imageUrl = "https://static.standard.co.uk/s3fs-public/thumbnails/image/2019/07/16/13/sub-cult-1607.jpg?width=640&auto=webp&quality=100&crop=1500%3A1000%2Csmart",
        description = "When hunger hits, there are few substitutes for a sub: if you need your sandwich to go long, Sub Cult’s super-sized American snacks hit the spot."
    )

    restaurant23 = Restaurant(
        ownerId=2,
        name="Cheesecake Factory",
        address="123 Main Street",
        cuisineType="American",
        priceRange="$$$",
        imageUrl="https://hips.hearstapps.com/hmg-prod/images/7-for-20-1592927899.jpg",
        description="American chain restaurant offering sizable portions from a vast menu including signature cheesecake"
    )

    restaurant24 = Restaurant(
        ownerId=2,
        name="BBQ Shack",
        address="456 Elm Street",
        cuisineType="American",
        priceRange="$$",
        imageUrl="https://www.telegraph.co.uk/multimedia/archive/03352/bbqblues_3352294b.jpg?imwidth=680",
        description="BBQ Shack is a renowned American barbecue restaurant known for its tender smoked meats and flavorful sauces."
    )

    restaurant25 = Restaurant(
        ownerId=2,
        name="TGI Friday's",
        address="789 Oak Avenue",
        cuisineType="American",
        priceRange="$$",
        imageUrl="https://cdn.vox-cdn.com/thumbor/HHjlXmcYDNMvW8XFY33odYG59ZE=/0x0:4543x2870/1200x675/filters:focal(1909x1072:2635x1798)/cdn.vox-cdn.com/uploads/chorus_image/image/56969031/tgifriday_8602.0.jpg",
        description="Casual chain restaurant with a festive vibe serving beer, cocktails & a wide menu of American fare."
    )

    restaurant26 = Restaurant(
        ownerId=2,
        name="Diner Deluxe",
        address="10 Maple Lane",
        cuisineType="American",
        priceRange="$",
        imageUrl="https://vhr-public-oregon.s3.us-west-2.amazonaws.com/poi_image/thumbnail/DYARDcC4wreUWQnbI3Rnr9NcpLbVuqV3",
        description="Diner Deluxe is a charming retro-style diner that captures the essence of classic American comfort food."
    )

    restaurant27 = Restaurant(
        ownerId=2,
        name="LongHorn",
        address="555 Oak Street",
        cuisineType="American",
        priceRange="$$$$",
        imageUrl="https://d1ralsognjng37.cloudfront.net/079dbde2-71ff-4e38-985e-8f505c562585.jpeg",
        description="Premium American steakhouse that offers top-quality cuts of beef cooked to perfection."
    )


    restaurant28 = Restaurant(
        ownerId=2,
        name="Golden Dragon",
        address="123 Main Street",
        cuisineType="Chinese",
        priceRange="$",
        imageUrl="https://d1ralsognjng37.cloudfront.net/48492e64-53f8-4a92-93d2-fd025fbc4c03.jpeg",
        description="Golden Dragon is a popular Chinese restaurant known for its authentic flavors and extensive menu."
    )

    restaurant29 = Restaurant(
        ownerId=2,
        name="Szechuan Palace",
        address="456 Elm Street",
        cuisineType="Chinese",
        priceRange="$$$$",
        imageUrl="https://d1ralsognjng37.cloudfront.net/50df9974-b277-43d9-886e-dc8cddcdca31.jpeg",
        description="Szechuan Palace specializes in Szechuan cuisine, known for its bold and spicy flavors."
    )

    restaurant30 = Restaurant(
        ownerId=2,
        name="Dragon Wok",
        address="789 Oak Avenue",
        cuisineType="Chinese",
        priceRange="$$$",
        imageUrl="https://d1ralsognjng37.cloudfront.net/4a5b2ec9-db83-4ea7-bad0-10f62f78eb14.jpeg",
        description="Dragon Wok offers a wide selection of Chinese stir-fry dishes made with fresh ingredients and flavorful sauces."
    )

    restaurant31 = Restaurant(
        ownerId=2,
        name="Peking Garden",
        address="10 Maple Lane",
        cuisineType="Chinese",
        priceRange="$$",
        imageUrl="https://d1ralsognjng37.cloudfront.net/03b6c2cb-6f39-4291-9e41-1f909dc09036",
        description="Peking Garden is a charming Chinese restaurant that specializes in Beijing-style cuisine. "
    )

    restaurant32 = Restaurant(
        ownerId=2,
        name="Rome Eats",
        address="123 Main Street",
        cuisineType="Italian",
        priceRange="$$",
        imageUrl="https://www.tastingtable.com/img/gallery/20-italian-dishes-you-need-to-try-at-least-once/l-intro-1643403830.jpg",
        description="Cozy Italian restaurant that offers a delightful selection of classic Italian dishes."
    )

    restaurant33 = Restaurant(
        ownerId=2,
        name="Pasta Paradise",
        address="789 Oak Avenue",
        cuisineType="Italian",
        priceRange="$",
        imageUrl="https://images.squarespace-cdn.com/content/v1/5e484ab628c78d6f7e602d73/1599248222831-ZMHAFYJT9T3IXH3IVGKY/What-to-eat-in-Italy.png",
        description="Pasta Paradise is a casual Italian eatery that celebrates the simplicity and comfort of Italian cuisine."
    )


    restaurant34 = Restaurant(
        ownerId=2,
        name="Sakura Sushi",
        address="123 Main Street",
        cuisineType="Sushi",
        priceRange="$$",
        imageUrl="https://d1ralsognjng37.cloudfront.net/b68bc980-98f3-437d-aac2-492e0cbaccea.jpeg",
        description="Sakura Sushi is a popular sushi restaurant known for its fresh and beautifully crafted sushi rolls."
    )

    restaurant35 = Restaurant(
        ownerId=2,
        name="Sushi Heaven",
        address="456 Elm Street",
        cuisineType="Sushi",
        priceRange="$$$",
        imageUrl="https://duyt4h9nfnj50.cloudfront.net/resized/f8d2019583140bab86b5dff8db74a22c-w2880-9e.jpg",
        description="Sushi Heaven is a high-end sushi restaurant that offers an elevated dining experience."
    )

    restaurant36 = Restaurant(
        ownerId=2,
        name="Zen Sushi Bar",
        address="789 Oak Avenue",
        cuisineType="Sushi",
        priceRange="$$$$",
        imageUrl="https://duyt4h9nfnj50.cloudfront.net/resized/36ead037fb04be3ff38ad1ba5b63cb43-w2880-0c.jpg",
        description="Zen Sushi Bar is a casual and relaxed sushi spot that delivers on taste and quality."
    )

    restaurant37 = Restaurant(
        ownerId=2,
        name="Green Leaf Bistro",
        address="123 Main Street",
        cuisineType="Healthy",
        priceRange="$$",
        imageUrl="https://i.ytimg.com/vi/AYG1REWFYmY/maxresdefault.jpg",
        description="Green Leaf Bistro is a popular healthy restaurant that specializes in fresh, organic, and nutritious dishes."
    )

    restaurant38 = Restaurant(
        ownerId=2,
        name="Fit Kitchen",
        address="456 Elm Street",
        cuisineType="Healthy",
        priceRange="$",
        imageUrl="https://cdn.squaremeal.co.uk/article/9484/images/healthy-london-ve-kitchen_01122021110525.jpg?w=1200",
        description="Fit Kitchen is a dedicated healthy eatery that caters to health-conscious individuals."
    )

    restaurant39 = Restaurant(
        ownerId=2,
        name="Fresh Fusion",
        address="789 Oak Avenue",
        cuisineType="Healthy",
        priceRange="$$$",
        imageUrl="https://tb-static.uber.com/prod/image-proc/processed_images/fa97d8601a03d3ac5cab878982fd98a8/3ac2b39ad528f8c8c5dc77c59abb683d.jpeg",
        description="Fresh Fusion is a vibrant and innovative healthy restaurant that offers a fusion of flavors and culinary styles."
    )

    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(restaurant3)
    db.session.add(restaurant4)
    db.session.add(restaurant5)
    db.session.add(restaurant6)
    db.session.add(restaurant7)
    db.session.add(restaurant8)
    db.session.add(restaurant9)
    db.session.add(restaurant10)
    db.session.add(restaurant11)
    db.session.add(restaurant12)
    db.session.add(restaurant13)
    db.session.add(restaurant14)
    db.session.add(restaurant15)
    db.session.add(restaurant16)
    db.session.add(restaurant17)
    db.session.add(restaurant18)
    db.session.add(restaurant19)
    db.session.add(restaurant20)
    db.session.add(restaurant21)
    db.session.add(restaurant22)
    db.session.add(restaurant23)
    db.session.add(restaurant24)
    db.session.add(restaurant25)
    db.session.add(restaurant26)
    db.session.add(restaurant27)
    db.session.add(restaurant28)
    db.session.add(restaurant29)
    db.session.add(restaurant30)
    db.session.add(restaurant31)
    db.session.add(restaurant32)
    db.session.add(restaurant33)
    db.session.add(restaurant34)
    db.session.add(restaurant35)
    db.session.add(restaurant36)
    db.session.add(restaurant37)
    db.session.add(restaurant38)
    db.session.add(restaurant39)
    db.session.commit()


def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))
    db.session.commit()

