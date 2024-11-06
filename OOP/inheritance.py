# Base class
from urllib.request import parse_http_list


class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

# Subclass
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class camel(Animal):
    def whipping(self):
        print("Camel is whipping")



class cat(Animal):
    def meow(self):
        print("Cat is meowing")


class donkey(Animal):
            def parking(self):
                print("Donkey is Parking")

# Creating an instance of Dog
my_dog = Dog()
park = donkey()
park1 = cat()
park2= camel()

# Using inherited methods from Animal
my_dog.eat()    # Output: Animal is eating
my_dog.sleep()  # Output: Animal is sleeping

# Using the new method in Dog
my_dog.bark()   # Output: Dog is barking
park.parking()
park1.meow()
park2.whipping()


