def sort_array_desc(array):
    array.sort(reverse=True)
    return array
array = [5, 2, 8, 7, 1]
sorted_array = sort_array_desc(array)
print(sorted_array)