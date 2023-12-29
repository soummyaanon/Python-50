# import the math library
import math
 
# function to print all
# non-primes in a range
def is_not_prime(n):
 
    # flag to track
    # if no. is prime or not
    # initially assume all numbers are
    # non prime
    flag = False
 
    # iterate in the given range
    # using for loop starting from 2
    # as 0 & 1 are neither prime
    # nor composite
    for i in range(2, int(math.sqrt(n)) + 1):
 
        # condition to check if a
        # number is prime or not
        if n % i == 0:
            flag = True
    return flag
 
# lower bound of the range
range_starts = 10
 
# upper bound of the range
range_ends = 30
print("Non-prime numbers between",range_starts,"and", range_ends,"are:")
 
for number in filter(is_not_prime, range(range_starts, range_ends)):
    print(number)
