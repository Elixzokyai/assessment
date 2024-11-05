class Calculator:
    # Static attribute to count the number of times add() is called
    count = 0

    @staticmethod
    def add(a, b):
        # Increment the count each time add() is called
        Calculator.count += 1
        return a + b

# Example usage of the Calculator class
if __name__ == "__main__":
    # Using the static method add()
    result1 = Calculator.add(5, 10)
    print(f"Result of addition: {result1}")
    print(f"Add method called: {Calculator.count} times")

    result2 = Calculator.add(3, 7)
    print(f"Result of addition: {result2}")
    print(f"Add method called: {Calculator.count} times")
