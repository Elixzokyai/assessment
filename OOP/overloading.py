class Rectangle:
    def __init__(self, length, width=None):
        # If width is not provided, assume it's a square
        if width is None:
            self.length = length
            self.width = length
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width


# Testing the Rectangle class
# Create a square
square = Rectangle(5)
print("Square area:", square.area())  # Output should be 25

# Create a general rectangle
rectangle = Rectangle(5, 10)
print("Rectangle area:", rectangle.area())  # Output should be 50
