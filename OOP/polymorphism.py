class Cat:
    def make_sound(self):
        print("Meow!")

class Dog:
    def make_sound(self):
        print("Woof!")

# Function to demonstrate polymorphism
def animal_sound(animal):
    animal.make_sound()

# Creating instances of Cat and Dog
cat = Cat()
dog = Dog()

# Demonstrating polymorphism
animal_sound(cat)  # Output: Meow!
animal_sound(dog)  # Output: Woof!
