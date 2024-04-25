#!/usr/bin/python3
""" Console module for AirBnB """
import cmd
from models.user import User
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the console AirBnB"""
    prompt = "(hbnb) "

    all_classes = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]

    def do_EOF(self, arg):
        """Ctrl-D to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn't execute anything\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance:
Usage: create <class name>\n"""
        classes = {
            "User": User
        }
        if self.valid(arg):
            args = arg.split()
            if args[0] in classes:
                new = classes[args[0]]()
                new.save()
                print(new.id)

    def do_destroy(self, arg):
        """Deletes an instance
Usage: destroy <class name> <id>\n"""
        if self.valid(arg, True):
            args = arg.split()
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key in objects:
                del objects[obj_key]
                storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
Usage: show <class name> <id>\n"""
        if self.valid(arg, True):
            args = arg.split()
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key in objects:
                print(objects[obj_key])

    def do_all(self, arg):
        """Prints all string representation of all instances
Usage1: all
Usage2: all <class name>\n"""
        objects = storage.all()
        if arg:
            if arg in self.all_classes:
                print([str(obj) for obj in objects.values()
                       if type(obj).__name__ == arg])
            else:
                print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute
Usage: update <class name> <id> <attribute name> \"<attribute value>\"\n"""
        if self.valid(arg, True, True):
            args = arg.split()
            obj_key = args[0] + "." + args[1]
            objects = storage.all()
            if obj_key in objects:
                obj = objects[obj_key]
                attr_name = args[2]
                if len(args) >= 4:
                    attr_value = args[3]
                    setattr(obj, attr_name, attr_value)
                    storage.save()
                else:
                    print("** value missing **")
            else:
                print("** no instance found **")

    def valid(self, arg, id_flag=False, att_flag=False):
        """validation of argument that pass to commands"""
        args = arg.split()
        _len = len(args)
        if _len == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.all_classes:
            print("** class doesn't exist **")
            return False
        if _len < 2 and id_flag:
            print("** instance id missing **")
            return False
        if id_flag and args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
            return False
        if _len == 2 and att_flag:
            print("** attribute name missing **")
            return False
        if _len == 3 and att_flag:
            print("** value missing **")
            return False
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

