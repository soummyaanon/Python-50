def insert_into_sorted_list(sorted_list, element):
    sorted_list.append(element)
    sorted_list.sort()
    return sorted_list

sorted_list = input("Enter the sorted list: ").split()
element = input("Enter the element to insert: ")

print(insert_into_sorted_list(sorted_list, element))
