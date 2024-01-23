def insert_into_sorted_list(sorted_list, element):
    sorted_list.append(element)
    sorted_list.sort()
    return sorted_list



print(insert_into_sorted_list([1,2,3,5,6], 4))