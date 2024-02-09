from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """A base class for all other classes."""
    def __init__(self, **kwargs):
        """Instance initializer."""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs.keys():
                if key == 'created_at' or key == 'updated_at':
                    kwargs[key] = datetime.strptime(kwargs[key],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, kwargs[key])
                elif key != '__class__':
                    setattr(self, key, kwargs[key])

    def save(self):
        """Save instance with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        Dictionnaire = self.__dict__.copy()
        Dictionnaire["created_at"] = self.created_at.isoformat()
        Dictionnaire["updated_at"] = self.updated_at.isoformat()
        Dictionnaire["__class__"] = self.__class__.__name__
        return Dictionnaire

    def __str__(self):
        """A string representation of an object using the method __str__"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
