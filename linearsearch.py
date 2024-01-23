def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# Prompt the user to enter the array as a list of integers
array = [int(i) for i in input("Enter the array: ").split(',')]

# Prompt the user to enter the target value
target = int(input("Enter the target value: "))

# Call the linear_search function and print the result
print(linear_search(array, target))
