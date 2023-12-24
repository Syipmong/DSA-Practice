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

numbers = [1,2,3,4,5,6,7,8]

print(binary_search(numbers,9))

