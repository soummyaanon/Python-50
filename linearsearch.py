def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# Test the function
print(linear_search([1, 2, 3, 4, 5], 3))