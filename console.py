#!/usr/bin/python3
""" This module contain program that contains the entry point of the command
interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ A class coontain the entry point of the command interpreter
    Attributes:
        prompt(str): prompt string
    """
    prompt = "(hbnb) "

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
