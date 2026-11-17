#!/usr/bin/python3
"""Module that defines the Base class shared by every model."""
import csv
import json
import os


class Base:
    """Manage the id attribute for all model classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a model and assign its public id.

        Args:
            id: The public id. A new id is generated when this is None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries.

        Args:
            list_dictionaries: Dictionaries to serialize.

        Returns:
            The JSON string, or "[]" when the list is missing or empty.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to a file.

        Args:
            list_objs: Instances that inherit from Base, or None.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            dictionaries = []
        else:
            dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string: A JSON string of a list of dictionaries.

        Returns:
            The decoded list, or an empty list when the string is missing.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance with every attribute already set.

        Args:
            dictionary: Attribute names and values for the new instance.

        Returns:
            An instance of the current class.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return the instances stored in the class JSON file.

        Returns:
            A list of instances, or an empty list when the file is missing.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as file:
            dictionaries = cls.from_json_string(file.read())
        return [cls.create(**dictionary) for dictionary in dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file.

        Args:
            list_objs: Instances that inherit from Base, or None.
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator="\n")
            if list_objs is None:
                return
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                writer.writerow([dictionary[field] for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return the instances stored in the class CSV file.

        Returns:
            A list of instances, or an empty list when the file is missing.
        """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        instances = []
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                dictionary = {}
                for index, field in enumerate(fields):
                    dictionary[field] = int(row[index])
                instances.append(cls.create(**dictionary))
        return instances
