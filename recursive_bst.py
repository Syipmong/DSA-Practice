def recursive_binary(list, value):
    if len(list) == 0:
        return False
    else:
        mid = (len(list))//2
        if list[mid] == value:
            return True
        else:
            if list[mid] < value:
                return recursive_binary(list[mid+1:],value)
            else:
                return recursive_binary(list[:mid],value)
    return False



def verify(bool):
    if bool == True:
        return "Index Found"
    return "Index Not found"


list = [1,2,3,4,5,6,7,8]
