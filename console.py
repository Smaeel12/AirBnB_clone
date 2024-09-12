#!/usr/bin/python3
"""
A consol to create and update objects
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the console class"""
    prompt = '(hbnb) '
    __classes = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    def do_create(self, line):
        """creates a new instance of a specified class and prints its ID"""
        clss = line.split()
        if clss:
            try:
                obj = eval(clss[0] + '()')
                storage.new(obj)
                storage.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id."""
        if line:
            line = line.split()
            if line[0] in self.__classes:
                try:
                    ins = storage.all().get(
                        "{}.{}".format(line[0], line[1]), None)
                    if ins:
                        print(ins)
                    else:
                        print("** no instance found **")
                except Exception:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_destroy(self, line):
        """Deletes an instance based on the class
        name and id (save the change into the JSON file)."""
        if line:
            line = line.split()
            if line[0] in self.__classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                    ins = storage.all().get(key, None)
                    if ins:
                        ins = storage.all().pop(key, None)
                        storage.save()
                    else:
                        print("** no instance found **")
                except Exception:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name."""
        objs = storage.all()
        try:
            clss = line.split()[0]
            if clss in self.__classes:
                ls = [str(obj) for obj in objs.values()
                      if obj.to_dict()['__class__'] == clss]
                if ls:
                    print(ls)
            else:
                print("** class doesn't exist **")
        except Exception:
            print([str(obj) for obj in objs.values()])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating an attribute
        (save the change into the JSON file).
        """
        if line:
            line = line.split()
            if line[0] in self.__classes:
                try:
                    ins = storage.all().get(
                        "{}.{}".format(line[0], line[1]), None)
                    if ins:
                        if len(line) > 2:
                            if (len(line) > 3):
                                setattr(ins, line[2], line[3].strip('"'))
                                storage.save()
                            else:
                                print('** value missing **')
                        else:
                            print('** attribute name missing **')
                    else:
                        print("** no instance found **")
                except Exception:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        print(len([obj for obj in storage.all().values() if obj.to_dict()[
            '__class__'] == line.split()[0]]))

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def precmd(self, line) -> str:
        """Hook method executed just before the command line is
        interpreted, but after the input prompt is generated and issued.
        """
        if ('.' in line):
            clss, _, cmd = line.partition('.')
            if cmd.endswith('()'):
                return "{} {}".format(cmd[:-2], clss)
            else:
                cmd, arg = cmd[:cmd.index(
                    '(')], cmd[cmd.index('(') + 1:cmd.index(')')]
                cid, _, params = arg.partition(', ')
                cid = cid.strip('"')
                if params:
                    if isinstance(eval(params), dict):
                        params = eval(params)
                        func = getattr(self, 'do_' + cmd)
                        for attr, val in params.items():
                            print(attr, val)
                            func('{} {} {} {}'.format(clss, cid, attr, val))
                        return ''
                    return '{} {} {} {}'.format(cmd, clss, cid, params)
                return '{} {} {}'.format(cmd, clss, cid)
        return line

    def emptyline(self):
        """handling ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
