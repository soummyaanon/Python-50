# given list of numbers
num_list = [1,3,5,6,99,134,55]
 
 
# iterate through the list elemets
# using for loop
for i in num_list:
 
    # if divided by 2, all even
    # number leave a remainder of 0
    if i%2==0:
        print(i,"is an even number.")
 
    # if remainder is not zero
    # then it's an odd number
    else:
        print(i,"is an odd number.")
