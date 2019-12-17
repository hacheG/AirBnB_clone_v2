#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __table__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

# esto lo comente por que molestaba para la ejecucion del 7
#    @property
#    def cities(self):
