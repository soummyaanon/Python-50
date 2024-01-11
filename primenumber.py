num1 = int(input("Enter any Number:"))
k=0
if num1 == 0 or num1==1:
    print("Not a prime number")
else:
    i = 2
    while(i<num1):
        if num1 % i== 0:
            k = k+1
            i = i+1

if k == 0:
    print(num1, "is prime number")
else:
    print(num1, "is not prime number")
    