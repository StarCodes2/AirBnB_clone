#!/usr/bin/python3
"""Defines a line-oriented command interpreter for the AirBnB clone project."""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines methods for the commands allowed by the interpreter."""

    prompt = "(hbnb) "
    __cls = {"BaseModel",
             "User",
             "Place",
             "State",
             "City",
             "Amenity",
             "Review"}

    def do_create(self, class_name):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
         prints its id."""
        if class_name:
            try:
                new = eval(class_name + "()")
                new.save()
                print(new.id)
            except NameError:
                print("** class doesn't exist **")
            except SyntaxError:
                print("** class name missing **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance based on its class
           name and id."""
        if line:
            args = line.split(" ")
            if args[0] not in self.__cls:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                objs = storage.all()
                key = args[0] + "." + args[1]
                if key in objs:
                    print(objs[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Destroy's an object. Usage: destroy <ClassName> <Object id>"""
        if line:
            args = line.split(" ")
            if args[0] not in self.__cls:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                objs = storage.all()
                key = args[0] + "." + args[1]
                if key in objs:
                    del objs[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
           on the class name."""
        objs = storage.all()
        if line:
            if line not in self.__cls:
                print("** class doesn't exist **")
            else:
                result = [str(obj) for obj in objs.values()
                          if obj.__class__.__name__ == line]
                print(result)
        else:
            result = [str(obj) for obj in objs.values()]
            print(result)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        try:
            if not line:
                raise SyntaxError()
            value = line.split('"')
            args = value[0].split(" ")
            if len(value) > 1 and len(args) > 3 and args[3] == "":
                args[3] = '"' + value[1] + '"'

            if args[0] not in self.__cls:
                raise NameError()
            if len(args) < 2 or args[1] == "":
                raise IndexError()
            if len(args) < 3 or args[2] == "":
                raise AttributeError()
            if len(args) < 4:
                raise ValueError()

            objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in objs:
                print("** no instance found **")
            else:
                try:
                    objs[key].__dict__[args[2]] = eval(args[3])
                except Exception:
                    objs[key].__dict__[args[2]] = args[3]
                objs[key].save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def do_quit(self, line):
        "Quit command to exit the program."
        return True

    def do_EOF(self, line):
        "EOF command to exit the program."
        return True

    def count(self, line):
        """Counts the number of instance of a given class that exist."""
        count = 0
        if line not in self.__cls:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            for key in objs:
                class_name = key.split(".")
                if class_name[0] == line:
                    count += 1
            print(count)

    def emptyline(self):
        """Overrides the base class method emptyline() to do nothing."""
        pass

    def default(self, line):
        """Overrides the default() methods to use custom commands."""
        args = line.split(".")
        if len(args) > 1:
            if (args[1] == "all()"):
                self.do_all(args[0])
            elif (args[1] == "count()"):
                self.count(args[0])
        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
