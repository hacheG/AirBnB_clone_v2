#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy.orm import relationship, backref
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""

    places = relationship("place", cascade="all,delete", backref="cities")
