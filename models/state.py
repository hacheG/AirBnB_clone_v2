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
<<<<<<< HEAD
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        x = []
        for value in models.storage.all(City).values():
            if value.state_id == self.id:
                x.append(value)
        return x
=======
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

# esto lo comente por que molestaba para la ejecucion del 7
#    @property
#    def cities(self):
>>>>>>> 61e3f1dd5fb0df625cd8e8f0b8a031e4cb9b5d4e
