def gcd (a,b):
    if (a == 0):
        return b
    if (b ==0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD of", a, "and", b, "is", gcd(a,b))