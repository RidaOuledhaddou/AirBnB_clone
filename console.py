#!/usr/bin/python3
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from shlex import split


class HBNBCommand(cmd.Cmd):
    """class for console file for airbnb"""
    prompt = "(HBNB)"
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }
    __attributes = {
        "email",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_EOF(self, arg):
        """Ctrl-D to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything\n"""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create command lets you create a new class
        instance and print a unique id.
        """
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            Classe = arg.split()[0]
            if Classe in HBNBCommand.__classes:
                class_obj = HBNBCommand.__classes[Classe]
                instance = class_obj()
                print(instance.id)
                storage.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Show command lets you display the string
        representation of an instance with a given id.
        """
        args = arg.split()
        objet = storage.all()
        length = len(args)
        if length == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objet:
            print("** no instance found **")
        else:
            print(objet["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Destroy command lets you delete an instance of
        a class with a given id."""
        args = arg.split()
        objet = storage.all()
        length = len(args)
        if length == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objet:
            print("** no instance found **")
        else:
            del objet["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances
        of a given class or if you run just 'all', it displays
        string representations of all instances.
        """
        args = arg.split()
        length = len(args)
        if length > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objet = []
            for obj in storage.all().values():
                if length > 0 and args[0] == obj.__class__.__name__:
                    objet(obj.__str__())
                elif length == 0:
                    objet.append(obj.__str__())
            print(objet)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = split(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Handle invalid input."""
        dictionnary = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        args = re.search(r"\.", arg)
        if args is not None:
            argument = [arg[: args.span()[0]], arg[args.span()[1]:]]
            args = re.search(r"\((.*?)\)", argument[1])
            if args is not None:
                command = [argument[1][: args.span()[0]], args.group()[1:-1]]
                if command[0] in dictionnary.keys():
                    call = "{} {}".format(argument[0], command[1])
                    return dictionnary[command[0]](call)
        print("*** Unknown command: {}".format(arg))
        return False

    def do_update(self, arg):
        """Update method to update an attribute in a object"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objet = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objet.keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instance = objet[key]
                attr_type = type(getattr(instance, args[2], ''))
                setattr(instance, args[2], attr_type(args[3]))
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
