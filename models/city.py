#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities")
