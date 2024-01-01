given_range = 25

#iterate using the forloop till the given range 

for i in range (given_range+1):

    #if no. is mulitiple of 4 and 5
    # print Hello github 
    if i % 4 == 0 and i % 5 == 0:
        print("Hello-Gihub")

        continue
    if i % 4 == 0 and i % 5!=0:
        print("Hello")

        continue
    if i % 5==0 and i % 4!=0:
        print("gihub")
    else:
        
        print(i)



