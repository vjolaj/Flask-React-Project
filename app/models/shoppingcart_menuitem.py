from .db import db, environment, SCHEMA, add_prefix_for_prod

shoppingCart_menuItems = db.Table(
    "shoppingCart_menuItems",
    db.Column(
        "shoppingCartId",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("shoppingCarts.id")),
        primary_key=True
    ),
    db.Column(
        "menuItemId",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("menuitems.id")),
        primary_key=True
    )
    
)
if environment == "production":
    shoppingCart_menuItems.schema = SCHEMA