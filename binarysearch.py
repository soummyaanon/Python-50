def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1 

arr = [1,2,3,4,5,6,7,8,9,10]
target = 5

result  = binary_search(arr, target)

if result != -1: 
    print("Element is present at index %d" % result) 
else:
    print("Element is not present in array")