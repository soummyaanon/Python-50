# Encapsulation
class Encapsulation(object):# This is a class
    def __init__(self, a, b, c):# This is a constructor
        self.public = a  # This is a public variable
        self._protected = b # This is a protected variable
        self.__private = c # This is a private variable

# Method Overloading
class Overloading(object):# This is a class
    def add(self, a, b, c=0):# This is a method
        return a + b + c# This is a return statement

# Inheritance
class Parent(object):# This is a class
    def __init__(self, value):# This is a constructor
        self.value = value# This is a public variable

class Child(Parent):
    def get_value(self):
        return self.value

# Demonstrate encapsulation
e = Encapsulation(1, 2, 3)
print(e.public)
print(e._protected)
print(e._Encapsulation__private)

# Demonstrate method overloading
o = Overloading()
print(o.add(1, 2))
print(o.add(1, 2, 3))

# Demonstrate inheritance
c = Child(5)
print(c.get_value())