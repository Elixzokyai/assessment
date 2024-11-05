from abc import ABC, abstractmethod
import math


# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Subclass for Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


# Create instances of Circle and Square
circle = Circle(radius=5)
square = Square(side_length=4)

# Call area() on each instance
print(f"Area of the Circle: {circle.area():.2f}")  # Output the area of the circle
print(f"Area of the Square: {square.area():.2f}")  # Output the area of the square
