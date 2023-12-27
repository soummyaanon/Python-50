# if the given number is 10
given_number = 20

# set up a variable to store the sum with an initial value of 0
sum = 0

# since we want to include the number 10 in the sum
# increment each number from 1 to given_number in the for loop
for i in range(1, given_number + 1):
    sum += i

# print the total sum at the end
print(sum)
