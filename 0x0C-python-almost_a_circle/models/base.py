#!/usr/bin/python3
"""_summary_
"""
import json

from models.rectangle import Rectangle


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
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("")
            else:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        csv_line = "{},{},{},{},{}\n".format(
                            obj.id, obj.width, obj.height, obj.x, obj.y)
                    elif cls.__name__ == "Square":
                        csv_line = "{},{},{},{}\n".format(
                            obj.id, obj.size, obj.x, obj.y)
                    file.write(csv_line)

    @classmethod
    def load_from_file_csv(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                list_lines = file.readlines()
                list_dicts = []
                for line in list_lines:
                    list_values = line.rstrip('\n').split(',')
                    dict_values = {
                        "id": int(list_values[0]),
                        "width": int(list_values[1]),
                        "height": int(list_values[2]),
                        "x": int(list_values[3]),
                        "y": int(list_values[4])
                    } if cls.__name__ == "Rectangle" else {
                        "id": int(list_values[0]),
                        "size": int(list_values[1]),
                        "x": int(list_values[2]),
                        "y": int(list_values[3])
                    }
                    list_dicts.append(dict_values)
                    return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []