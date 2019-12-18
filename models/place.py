#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
import os

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False)
                      Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
                      )

class Place(BaseModel, Base):
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    """if os.getenv("HBNB_TYPE_STORAGE") == "db":
    reviews = relationship("Review", cascade="all,delete", backref="place")
    amenities = relationship(
                "Amenity", secondary="place_amenity", viewonly=False)"""

    @property
    def reviews(self):
        """getter that returns the list of review inst"""
        reviewInstances = []
        for key, value in storage.items():
            if type(value).__name__ == "Review":
                reviewInstances.append(value)
        return (reviewInstances)

    @property
    def amenities(self):
        """getter that returns the list of amenity"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        if type(obj).__name__ == "Amenity":
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj)

