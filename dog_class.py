class Dog:
    # A simple attempt to model a dog
    def __init__(self, name, age):
        # Initialize name and age attributes.
        self.name = name
        self.age = age

    def sit(self):
        # Simulate a dog is sitting
        print(f"{self.name} is now sitting")

    def roll_over(self):
        # Simulate a dog is rolling over
        print(f"{self.name} rolled over!")
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
your_dog.roll_over()
my_dog.sit()
my_dog.roll_over()