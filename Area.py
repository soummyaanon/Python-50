import math


def area_of_circle(radius):
    return math.pi * radius **2

def area_of_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)


radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

print(area_of_circle(radius))
print(area_of_cylinder(radius, height))