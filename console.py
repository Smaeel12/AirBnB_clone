#!/usr/bin/python3
""" This module contain program that contains the entry point of the command
interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ A class coontain the entry point of the command interpreter
    Attributes:
        prompt(str): prompt string
    """
    prompt = "(hbnb) "

    # Create Command
    def do_create(self, line):
        """ Creates a new instance of BaseModel
        """
        if (line == 'BaseModel'):
            obj = BaseModel()
            obj.save()
            print(obj.id)
        elif (len(line) == 0):
            print("** class name missing **")
        else:
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
        if (len(cmd_p) >= 1 and cmd_p[0] != 'BaseModel'):
            print("** class doesn't exist **")
            return
        if (len(cmd_p) == 1):
            print("** instance id missing **")
            return
        if (storage.all().get(f'BaseModel.{cmd_p[1]}')):
            print(storage.all().get(f'BaseModel.{cmd_p[1]}'))
        else:
            print("** no instance found **")

    # Create Command
    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        """
        cmd_p = line.split()
        if (len(cmd_p) == 0):
            print("** class name missing **")
            return
        if (len(cmd_p) >= 1 and (cmd_p[0] != 'BaseModel')):
                print("** class doesn't exist **")
                return
        if (len(cmd_p) == 1):
                print("** instance id missing **")
                return
        if (len(cmd_p) >= 1 and (cmd_p[0] == 'BaseModel')):
            if (storage.all().get(f'BaseModel.{cmd_p[1]}')):
                storage.all().pop(f'BaseModel.{cmd_p[1]}')
                storage.save()
            else:
                print("** no instance found **")

    # Create Command
    def do_all(self, line):
        """ Prints all string representation of all instances based or not on
        the class name
        """
        if (line == 'BaseModel' or len(line) == 0):
            obj_list = [str(obj) for obj in storage.all().values()]
            print(obj_list)
        else:
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
        if (len(cmd_p) >= 1 and cmd_p[0] != 'BaseModel'):
                print("** class doesn't exist **")
        if (len(cmd_p) == 1):
                print("** instance id missing **")
                return
        if (len(cmd_p) >= 2 and not storage.all().get(f'BaseModel.{cmd_p[1]}')):
                print("** no instance found **")
                return
        if (len(cmd_p) == 2):
            print("** attribute name missing **")
            return
        if (len(cmd_p) == 3):
            print("** value missing **")
            return
        obj = storage.all().get(f'BaseModel.{cmd_p[1]}')
        setattr(obj, cmd_p[2], cmd_p[3])

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