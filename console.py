#!/usr/bin/python3
"""Defines a line-oriented command interpreter for the AirBnB clone project."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines methods for the commands allowed by the interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        "Quit command to exit the program."
        return True

    def do_EOF(self, line):
        "EOF command to exit the program."
        return True

    def emptyline(self):
        """Overrides the base class method emptyline() to do nothing."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
