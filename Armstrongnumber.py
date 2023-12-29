# The given number
given_number = 407

# Convert given number to string so that we can iterate through it
given_str = str(given_number)

# Store the length of the string for future use
string_length = len(given_str)

# Initialize a sum variable with 0 value to store the sum of the product of each digit
total_sum = 0

# Iterate through the given string
for digit in given_str:
    total_sum += int(digit) ** string_length

# Check if the sum matches the given number; it's an Armstrong number
if total_sum == given_number:
    print(f"The given number {given_number} is an Armstrong number.")
else:
    print(f"The given number {given_number} is not an Armstrong number.")

