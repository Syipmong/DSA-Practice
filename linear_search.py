def linear_search(list, value):
    for i in range(0, len(list)):
        if list[i] == value:
            return i
    return None

def verify_search(index):
    if index is not None:
        print("index found at: ", index)
    else:
        print("Index not found")


list = [1,2,3,4,5,6,7,8]

result = linear_search(list, 10)
print(verify_search(list))