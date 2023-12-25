def recursive_binary(list, value):
    # This function takes a sorted list and a search value as input. It returns the index of the value if it is in the list or -1
    mid = len(list)//2
    if list[mid] == value:
        return True
    else:
        if list[mid] < value:
            return recursive_binary(list[mid:], value)
        else:
            return recursive_binary(list[:mid],value)
    return False

list = [1,2,3,4,5,6,7,8]

print(recursive_binary(list,9))

def rec_bin(list, value):
    if len(list) == 0:
        return False
    