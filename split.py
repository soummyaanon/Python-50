def arbitrary_split(data, condition):
    list1 = [item for item in data if condition(item)]
    list2 = [item for item in data if not condition(item)]
    return list1, list2

# Example usage:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1, list2 = arbitrary_split(data, lambda x: x <= 5)

print("List1:", list1)
print("List2:", list2)
