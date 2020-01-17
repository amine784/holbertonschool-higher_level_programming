#!/usr/bin/python3
'''
function to set rectngle
widh
height
'''


class Rectangle:
    '''
    def method
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return(0)
        else:
            return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        space = ""
        sym = str(self.print_symbol)
        line = self.__height
        if self.__width == 0:
            return(space)
        if self.__height == 0:
            return(space)
        else:
            for h in range(line):
                for w in range(line - 1):
                    print(sym * self.__width)
                return (sym * self.__width)

    def __repr__(self):
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        x = 0
        y = 0
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        x = rect_1.area()
        y = rect_2.area()
        if x >= y:
            return(rect_1)
        if y > x:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        return(cls(size, size))
