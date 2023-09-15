#!/usr/bin/python3
""" Base class """
import json
import csv
import turtle


class Base:
    """ Base class """
    obj = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is None:
            Base.obj += 1
            self.id = Base.obj
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the list_dictionaries"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                list_instances = []
                for dict in list_dicts:
                    list_instances.append(cls.create(**dict))
                return list_instances
        except:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to file in csv format """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load from file in csv format """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in row.items())
                              for row in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw rectangles and squares """
        t = turtle.Turtle()
        t.color("green")
        t.screen.bgcolor("#b7312c")
        t.pensize(3)
        t.shape("turtle")

        t.color("white")
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        t.color("black")
        for square in list_squares:
            t.showturtle()
            t.up()
            t.goto(square.x, square.y)
            t.down()
            for i in range(2):
                t.forward(square.size)
                t.left(90)
                t.forward(square.size)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()