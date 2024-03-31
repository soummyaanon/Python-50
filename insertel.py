def insert_into_sorted_list(sorted_list, element):
    sorted_list.append(element)
    sorted_list.sort()
    return sorted_list

sorted_list = [1, 3, 5, 7, 9]  # Example sorted list
element = 4  # Example element to insert

print(insert_into_sorted_list(sorted_list, element))    # Output: [1, 3, 4, 5, 7, 9]

