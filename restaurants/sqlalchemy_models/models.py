#SQLAlchemy models definition.

from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants_restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    cuisine = Column(String)
    rating = Column(Float)
    phone = Column(String)
    email = Column(String)

# class Contact(Base):
#     __tablename__ = 'contacts'
#     id = Column(Integer, primary_key=True)
#     phone = Column(String)
#     email = Column(String)
#     restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
#     restaurant = relationship("Restaurant", back_populates="contact")

# Restaurant.contact = relationship("Contact", uselist=False, back_populates="restaurant")
