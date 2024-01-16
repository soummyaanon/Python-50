class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name}, and I am {self.age} years old.")

# Use the correct variable name here, it should be Person1 not person1
Person1 = Person("John", 30)

print("Name:", Person1.name)
print("Age:", Person1.age)
Person1.introduce()
