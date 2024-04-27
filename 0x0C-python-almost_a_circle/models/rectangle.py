#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base

# models/rectangle.py

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Call to the superclass to handle the ID
        self.width = width    # Validation will occur in the setter
        self.height = height  # Validation will occur in the setter
        self.x = x            # Validation will occur in the setter
        self.y = y            # Validation will occur in the setter

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Here you could add validation, e.g., value must be positive
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # Here you could add validation, e.g., value must be positive
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # Validation can also be done here, e.g., value must be non-negative
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        # Validation can also be done here, e.g., value must be non-negative
        self.__y = value
