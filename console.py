#!/usr/bin/python3
""" This module contain program that contains the entry point of the command
interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ A class coontain the entry point of the command interpreter
    Attributes:
        prompt(str): prompt string
    """
    prompt = "(hbnb) "
    __available_classes = [BaseModel, User, Place, State,
                           City, Amenity, Review]

    # Create Command
    def do_create(self, line):
        """ Creates a new instance of BaseModel
        """
        if (len(line) == 0):
            print("** class name missing **")
            return
        for value in HBNBCommand.__available_classes:
            if (line == value.__name__):
                obj = value()
                obj.save()
                print(obj.id)
                return
        print("** class doesn't exist **")

    # Create Command
    def do_show(self, line):
        """ Prints the string representation of an instance based on the class
        name and id
        """
        cmd_p = line.split()
        if (len(cmd_p) == 0):
            print("** class name missing **")
            return
        if (len(cmd_p) >= 1):
            for value in HBNBCommand.__available_classes:
                if (cmd_p[0] == value.__name__):
                    if (len(cmd_p) == 1):
                        print("** instance id missing **")
                        return
                    if (storage.all().get(f'{cmd_p[0]}.{cmd_p[1]}')):
                        print(storage.all().get(f'{cmd_p[0]}.{cmd_p[1]}'))
                        return
                    else:
                        print("** no instance found **")
                        return
        print("** class doesn't exist **")

    # Create Command
    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        """
        cmd_p = line.split()
        if (len(cmd_p) == 0):
            print("** class name missing **")
            return
        if (len(cmd_p) >= 1):
            for value in HBNBCommand.__available_classes:
                if (cmd_p[0] == value.__name__):
                    if (len(cmd_p) == 1):
                        print("** instance id missing **")
                        return
                    if (storage.all().get(f'{cmd_p[0]}.{cmd_p[1]}')):
                        storage.all().pop(f'{cmd_p[0]}.{cmd_p[1]}')
                        storage.save()
                        return
                    else:
                        print("** no instance found **")
                        return
        print("** class doesn't exist **")

    # Create Command
    def do_all(self, line):
        """ Prints all string representation of all instances based or not on
        the class name
        """
        if (len(line) == 0):
            obj_list = [str(obj) for obj in storage.all().values()]
            print(obj_list)
            return
        for value in HBNBCommand.__available_classes:
            if (line == value.__name__):
                obj_list = [str(obj) for obj in storage.all().values()]
                print(obj_list)
                return
        print("** class doesn't exist **")

    # Create Command
    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating attribute
        """
        cmd_p = line.split()
        if (len(cmd_p) == 0):
            print("** class name missing **")
            return
        for value in HBNBCommand.__available_classes:
            if (cmd_p[0] == value.__name__):
                if (len(cmd_p) == 1):
                    print("** instance id missing **")
                    return
                if (len(cmd_p) >= 2 and
                   not storage.all().get(f'{value.__name__}.{cmd_p[1]}')):
                    print("** no instance found **")
                    return
                if (len(cmd_p) == 2):
                    print("** attribute name missing **")
                    return
                if (len(cmd_p) == 3):
                    print("** value missing **")
                    return
                obj = storage.all().get(f'{value.__name__}.{cmd_p[1]}')
                setattr(obj, cmd_p[2], cmd_p[3])
                return
        print("** class doesn't exist **")

    # Emptyline Handling
    def emptyline(self):
        """ Emptyline handling
        """
        pass

    # Quit Command
    def do_quit(self, line):
        """ quit command
        """
        return True

    def help_quit(self):
        """ Show the help for quit command
        """
        print("Quit command to exit the program")

    # Ctrl+D Command
    def do_EOF(self, line):
        """ EOF command
        """
        print()
        return True

    def help_EOF(self):
        """ Show the help for EOF command
        """
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
