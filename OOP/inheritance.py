# Base class
class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

# Subclass
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Creating an instance of Dog
my_dog = Dog()

# Using inherited methods from Animal
my_dog.eat()    # Output: Animal is eating
my_dog.sleep()  # Output: Animal is sleeping

# Using the new method in Dog
my_dog.bark()   # Output: Dog is barking
