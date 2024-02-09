#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns all objects"""
        return FileStorage.__objects

    def new(self, arg):
        """This method new sets a key for dictionary of the objects"""
        objet = arg.__class__.__name__
        FileStorage.__objects["{}.{}".format(objet, arg.id)] = arg

    def save(self):
        """The method save new objects as str in json file"""
        serialization = {}
        for k, v in FileStorage.__objects.items():
            serialization[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(serialization))
    def reload(self):
        """This method reload the dictionary from file"""
        try:
            with open(FileStorage.__file_path) as file:
                dictionnaire = json.load(file)
                for o in dictionnaire.values():
                    classe = o["__class__"]
                    del o["__class__"]
                    self.new(eval(classe)(**o))
        except FileNotFoundError:
            return
