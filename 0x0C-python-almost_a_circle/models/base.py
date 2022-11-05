#!/usr/bin/python3
"""Module base class
Creates a base class
id is always an int
"""
import json
from dataclasses import field
import turtle as t
import csv
from os.path import exists


class Base:
    """Base class

    Private attrs:
        __nb__objects: 0
    public instance:
        id
    """

    __nb__objects = 0

    def __init__(self, id=None):
        """initializes the class

        Args:
            id: class id assignment
        """

        self.id = 0
        if id is None:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string representation of the input"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON representation to a file"""
        if list_objs is None:
            with open(f'{cls.__name__}.json', 'w') as f:
                f.write('[]')
        else:
            a = []
            for i in list_objs:
                a.append(cls.to_dictionary(i))
            with open(f'{cls.__name__}.json', 'w') as f:
                f.write(cls.to_json_string(a))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectange':
            a = cls(1, 1)
        else:
            a = cls(1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """Return a list of instance"""
        if not exists(f'{cls.__name__}.json'):
            return []
        with open(f'{cls.__name__}.json', 'r')as f:
            a = cls.from_json_string(f.read())
        b = []
        for i in a:
            b.append(cls.create(**i))
        return b

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to a csv file"""
        if list_objs is None:
            with open(f'{cls.__name__}.json', 'w') as f:
                f.write('')
        else:
            a = []
            for i in list_objs:
                a.append(cls.to_dictionary(i))
            with open(f'{cls.__name__}.csv', 'w', newline='') as f:
                if cls.__name__ == 'Rectangle':
                    writer = csv.DictWriter(f, fieldnames=['id', 'width',
                                            'height', 'x', 'y'])
                else:
                    writer = csv.DictWriter(f, fieldnames=['id', 'size',
                                            'x', 'y'])
                writer.writeheader()
                writer.writerows(a)

    @classmethod
    def load_from_file_csv(cls):
        """Use csv file"""
        if not exists(f'{cls.__name__}.csv'):
            return []
        a = []
        with open(f'{cls.__name__}.csv', 'r') as f:
            obj_dict = csv.DictReader(f)
            for row in obj_dict:
                for k, v in row.items():
                    row.update({k: int(v)})
                a.append(cls.create(**row))
        return a

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw the squares and rectangles"""
        t.pensize(6)
        for i in list_rectangles:
            t.pu()
            t.goto(i.x * 4, i.y * 4)
            t.pd()
            for j in range(2):
                t.pencolor('green')
                t.fd(i.width * 4)
                t.rt(90)
                t.fd(i.height * 4)
                t.rt(90)
            for i in list_squares:
                t.pu()
                t.goto(i.x * 4, i.y * 4)
                t.pd()
                for j in range(4):
                    t.pencolor('red')
                    t.fd(i.size * 4)
                    t.rt(90)
            t.exitonclick()
