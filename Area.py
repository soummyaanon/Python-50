import math

def area_of_circle(radius):
    return math.pi * radius **2

def area_of_cylynder(radius, height):
    return 2 * math.pi * radius* (radius+height)

print(area_of_circle(10))
print(area_of_cylynder(10, 20))