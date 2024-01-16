class Animal:
    def __init__(self, species):
        self.species = species
    def display_species(self):
        print(f"i am an {self.species}")


class Machine:
    def __init__(self, brand):
        self.brand = brand
    def  display_brand(self):
        print(f"This is a{self.brand} machin")


class RoboDog(Animal,Machine):
    def __init__(self, name, species, brand):
        Animal.__init__(self ,species)
        Machine.__init__(self,brand)
        self.name = name

    def introduce(self):
        print(f" My name is {self.name}")
        self.display_species()
        self.display_brand()

robot_dog = RoboDog("mark560", "RoboDog", "Tsla")
robot_dog.introduce()
robot_dog.display_brand()
robot_dog.display_species()
       