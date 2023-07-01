from flask.cli import AppGroup
from .users import seed_users, undo_users
from .restaurants import seed_restaurants, undo_restaurants
from .reviews import seed_reviews, undo_reviews
from .menu_items import seed_menu_items, undo_menu_items
from .orders import seed_order, undo_order

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        
        undo_order()
        undo_menu_items()
        undo_reviews()
        undo_restaurants()
        undo_users()
        
    seed_users()
    seed_restaurants()
    seed_reviews()
    seed_menu_items()
    seed_order()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_order()
    undo_menu_items()
    undo_reviews()
    undo_restaurants()
    undo_users()    
    # Add other undo functions here