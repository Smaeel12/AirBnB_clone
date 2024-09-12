from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand
from models import storage


class ConsoleTestCase(unittest.TestCase):
    def setUp(self):
        self.DARGS = {
            'create BaseModel': (len(storage.all()), len(storage.all()) + 1),
            f'destroy BaseModel {list(storage.all().values())[-1].id}':
            (len(storage.all()) - 1, len(storage.all())),
        }
        self.SARGS = {
            'create': '** class name missing **\n',
            'create MyModel': "** class doesn't exist **\n",
            'show': '** class name missing **\n',
            'show MyModel': "** class doesn't exist **\n",
            'show BaseModel': '** instance id missing **\n',
            'show BaseModel 121212': '** no instance found **\n',
            'destroy': '** class name missing **\n',
            'destroy MyModel': "** class doesn't exist **\n",
            'destroy BaseModel': '** instance id missing **\n',
            'destroy BaseModel 121212': '** no instance found **\n',
            'all MyModel': "** class doesn't exist **\n",
        }

    def test_dynamic_args(self):
        for cmd, values in self.DARGS.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(cmd)
                self.assertGreater(values[1], values[0])

    def test_console_args(self):
        for cmd, expected in self.SARGS.items():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(cmd)
                self.assertEqual(f.getvalue(), expected)

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all')
            self.assertTrue(f.getvalue().split())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all BaseModel')
            self.assertTrue(f.getvalue().split())


if __name__ == '__main__':
    unittest.main()
