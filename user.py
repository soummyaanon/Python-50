# Initialize a variable 'i' to 1
i = 1

# Prompt the user to enter a number and store it in the variable 'num'
num = int(input("Enter any Number:"))

# Use a while loop to iterate from 1 to 10 (inclusive)
while i <= 10:
    # Print the multiplication table for the entered number
    # by multiplying it with the current value of 'i'
    print(num, "*", i, "=", num * i)
    
    # Increment the value of 'i' by 1 for the next iteration
    i = i + 1

# End of the program
