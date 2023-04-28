#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
# Path: models/engine/db_storage.py
# Compare this snippet from models/engine/db_storage.py:

    def __init__(self, path):
        self._path = path
        self._data = {}

    def add(self, obj):
        cls_name = obj.__class__.__name__
        if cls_name not in self._data:
            self._data[cls_name] = {}
        self._data[cls_name][obj.id] = obj
        with open(self._path, 'w') as f:
            json.dump(self._data, f)

    def get(self, cls, id):
        with open(self._path, 'r') as f:
            self._data = json.load(f)
        if cls.__name__ in self._data and id in self._data[cls.__name__]:
            return self._data[cls.__name__][id]
        return None

    def count(self, cls=None):
        with open(self._path, 'r') as f:
            self._data = json.load(f)
        if cls is not None:
            if cls.__name__ in self._data:
                return len(self._data[cls.__name__])
            return 0
        return sum(len(self._data[cls_name]) for cls_name in self._data)
