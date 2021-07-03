
def checkIfExist(arr: [int]) -> bool:
    i = 0

    while i < len(arr):
        if  arr[i] != 0 and arr[i] * 2 not in arr:
            i +=1
        elif  arr[i] == 0 and arr[i] * 2 not in arr:
            i +=1
        else:
            return True
    return False
            

checkIfExist([0,1])