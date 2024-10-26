"""
Implement a function that takes an array arr, a testVariable (containing the number to search) and 
currentIndex (containing the starting index) as parameters. This function should output the index 
of the first occurrence of testVariable in arr. If testVariable is not found in arr it should return -1.
"""

def search(arr, element, current, length):
    if current > length:
        return -1
    else:
        if current > length and arr[current] == element:
            return current
        else:
            return search(arr, element, current+1, length)
        

arr = [1,2,3,4,5,6]
print(search(arr, 7, 0, len(arr)))
