def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1

# Prompt the user to enter the array as a list of integers
array = [int(i) for i in input("Enter the array: ").split(',')]

# Prompt the user to enter the target value
target = int(input("Enter the target value: "))

# Call the linear_search function and print the result
print(linear_search(array, target))
