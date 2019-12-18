#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    #    __tablename__ = 'amenities'

<<<<<<< HEAD
    name = Column(String(128), nullalble=False))
    place_amenities = relationship("Place", backref="amenities")
=======
    #   name = Column(String(128), nullalble=False)
    name = ""
>>>>>>> 7039353de6cd3e6b6d1ab7bd04454efeed567a2d
