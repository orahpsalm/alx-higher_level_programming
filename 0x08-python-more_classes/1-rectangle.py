#!/usr/bin/python3

"""Class Documentation"""


class Rectangle:
    """Defines a class `Rectangle`."""

    def __init__(self, width=0, height=0):
        """Initialization of rectangle class.
        Args:
            width (int): rectangle width (or breadth) [default: 0]
            height (int): rectangle height [default: 0].
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns rectangle width."""
        return self.__width

    @property
    def height(self):
        """Returns rectangle height."""
        return self.__height

    @width.setter
    def width(self, width):
        """Sets rectangle width to `value`.
        Args:
            value (int): Width of rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Sets rectangle height to `value`.
        Args:
            value (int): Height of rectangle.
        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
