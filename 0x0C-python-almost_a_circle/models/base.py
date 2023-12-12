#!/usr/bin/python3
"""_summary_
"""
import json
import csv
import turtle


class Base:
    """_summary_
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_

        Returns:
            _type_: _description_
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """_summary_

        Args:
            json_string (_type_): _description_

        Returns:
            _type_: _description_
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """_summary_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """
        with open(cls.__name__ + ".csv", "w", encoding='utf-8') as f:
            list_dicts = list()
            for item in list_objs:
                list_dicts.append(item.to_dictionary())
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        ans = []
        with open(cls.__name__ + ".csv", "r") as f:
            reader = csv.DictReader(f)
            for line in reader:
                kwargs = dict(line)
                for key, val in kwargs.items():
                    kwargs[key] = int(val)
                ans.append(cls.create(**kwargs))
            return ans

    @staticmethod
    def draw(list_rectangles, list_squares):
        """_summary_

        Args:
            list_rectangles (_type_): _description_
            list_squares (_type_): _description_
        """
        my_t = turtle.Turtle()
        for rect in list_rectangles:
            my_t.setheading(0)
            my_t.penup()
            my_t.goto(rect.x, rect.y)
            my_t.pendown()
            my_t.forward(rect.width)
            my_t.right(90)
            my_t.forward(rect.height)
            my_t.right(90)
            my_t.forward(rect.width)
            my_t.right(90)
            my_t.forward(rect.height)
        for squ in list_squares:
            my_t.setheading(0)
            my_t.penup()
            my_t.goto(squ.x, squ.y)
            my_t.pendown()
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
            my_t.right(90)
            my_t.forward(squ.size)
        input()
