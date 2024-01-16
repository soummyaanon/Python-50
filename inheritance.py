class Animal:
    def __init__(self, species):
        self.species = species

    def display_species(self):
        print(f"I am a {self.species}.")

# Dog is derived from Animal
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog")
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Labrador is derived from Dog
class Labrador(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def display_info(self):
        print(f"My name is {self.name}, I am {self.age} years old, and I am a {self.color} Labrador.")

# Creating an instance of Labrador
labrador1 = Labrador("Max", 2, "Yellow")

# Accessing attributes and methods through multi-level inheritance
labrador1.display_species()  # Inherited from Animal
labrador1.bark()             # Inherited from Dog
labrador1.display_info()      # Defined in Labrador class
