# import numpy as np
# arr = np.array([1,2,3])
# arr = np.append(arr, [4])
# print("After push: ", arr)

# arr = np.delete(arr, -1)
# print("After pop: ", arr)

# arr = np.array([10, 20, 30, 40, 50])
# while len(arr) > 0:
#     popelement = arr[-1]
#     print("Popped element: ", popelement)
#     arr = np.delete(arr, -1)
#     print("After pop: ", arr)


# Q2
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = list(map(int, input("Enter sorted elements: ").split()))
key = int(input("Enter the element to search: "))
result = binary_search(arr, key)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")