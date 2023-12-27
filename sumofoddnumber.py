given_range = 10

# Set up a variable to store the sum
# with an initial value of 0
sum = 0

for i in range(given_range):

    # If i is odd, add it 
    # to the sum variable
    if i % 2 != 0:
        sum += i

# Print the final sum after the loop
print(sum)
