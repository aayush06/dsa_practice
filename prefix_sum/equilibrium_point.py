"""
Given an array arr[] of size n, find the index i such that the sum of elements to the left of i 
is equal to the sum of elements to the right of i.

arr = [1, 3, 5, 2, 2]
Equilibrium index: 2 (since 1+3 = 2+2)

"""

def calculate_equilibrium_index(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[i-1]+arr[i])
    n = len(arr)
    for j in range(len(result)):
        if result[j-1] == result[n-1]-result[j]:
            return j
    return -1
    
arr = [1,3,5,2,2]
print(calculate_equilibrium_index(arr))
