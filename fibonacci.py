n = int(input("How many terms You Want in fibonacci Series :"))
if n==1:
    print("1")
elif n == 2:
    print("1, 1")
elif n <= 0:
    print("Please enter positive number zGreater than 0")
else:
    ft = 1
    st =1
    print(ft, end="")
    print(st, end="")
    i = 2
    while(i<n):
        nt = ft+st
        print(nt, end = "")
        ft = st
        st = nt 
        i = i+1