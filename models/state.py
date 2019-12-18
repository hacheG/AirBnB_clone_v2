#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from models.storage import Storage
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref=backref("state", cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """Cities"""
        x = []
        for key, value in storage.all(City).items():
            if value.state_id == self.id:
                x.append(value)
        return x
