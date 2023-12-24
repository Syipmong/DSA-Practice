def binary_search(list, value):
    left = 0
    right = len(list) -1
    while (left <= right):
        mid = (left + right)//2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            left = mid +1
        else:
            right = mid -1
    return None


def verify(index):
    if index is not None:
        return f"Index found at {index}"
    return f"Index not found"







numbers = [1,2,3,4,5,6,7,8,11]
result = binary_search(numbers,12)

print(verify(result))
