class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the Dog class
dog1 = Dog("Buddy", 3)

# Accessing attributes and calling the bark method
print("Name:", dog1.name)
print("Age:", dog1.age)
dog1.bark()
