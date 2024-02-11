import json
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Base
from base import engine

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Load JSON data
with open('restaurants.json') as file:
    data = json.load(file)

# Iterate over JSON items and create Restaurant instances
for item in data:
    restaurant = Restaurant(
        id=item['id'],
        name=item['name'],
        location=item['location'],
        cuisine=item['cuisine'],
        rating=item['rating'],
        contact=item['contact'],
    )
    session.add(restaurant)

# Commit the session to insert items into the database
session.commit()
