def linear_search(list, value):
    for i in range(0, len(list)):
        if list[i] == value:
            return i
    return None


list = [1,2,3,4,5,6,7,8]

print(linear_search(list, 10))