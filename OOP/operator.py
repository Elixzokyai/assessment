class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Test the Vector class and operator overloading
if __name__ == "__main__":
    # Create two Vector objects
    vector1 = Vector(2, 3)
    vector2 = Vector(5, 7)

    # Add the two vectors
    result_vector = vector1 + vector2

    # Print the result
    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print(f"Result of addition: {result_vector}")
