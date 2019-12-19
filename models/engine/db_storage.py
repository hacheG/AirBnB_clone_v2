#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Create the engine(self.__engine)
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """
        Returns a dictionary
        """
        a = dict()
        clasesitas = ['State', 'City', 'Place', 'Review', 'Amenity', 'User']
        if cls is not None:
            objre = self.__session.query(cls.__name__).all()
            print("Esto esta botando el all del datastorage", objre)
            for obj in objre:
                print("en teoria esto es cada objeto", obj)
                print("el id en teoria obj.id", obj.id)
                a["["+cls.__name__+"]"+"."+obj.id] = obj
        else:
            for clase in clasesitas:
                objre = self.__session.query(eval(clase)).all()
                print("objre",objre)
                for obj in objre:
                    print("cada objeto cuando no hay clase", obj)
                    print("imprimirle llave", obj.id)
                    print("este es e nombre", obj.__dict__)
                    #a["["+type(obj).__name__+"]"+"."+obj.id] = obj
                    # key = "{}.{}".format(type(obj).__name__, obj.id)
        return a

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmake(expire_on_commit=False),
                                        bind=self.engine)()

    def delete(self, obj=None):
        """
        Deletes an object from objects
        """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """
        Close the session
        """
        self.__session.close()
