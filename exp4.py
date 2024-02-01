# Define a function called list_sum that takes in a parameter called num_list
def list_sum(num_list):
    # Check if the length of num_list is equal to 1
    if len(num_list) == 1:
        # If it is, return the only element in num_list
        return num_list[0]
    else:
        # If the length of num_list is greater than 1, recursively call list_sum
        # with the remaining elements of num_list (excluding the first element)
        # and add the first element to the sum of the remaining elements
        return num_list[0] + list_sum(num_list[1:])

# Call the list_sum function with a list of numbers [2, 4, 5, 6, 7]
print(list_sum([2, 4, 5, 6, 7]))