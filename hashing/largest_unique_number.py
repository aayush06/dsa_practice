"""
    Given an array of integers A, return the largest integer that only occurs once.

    If no integer occurs once, return -1.
    
Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
"""
arr = [9,9,8,8]
mapp = {}
for i in arr:
    if i in mapp:
        mapp.pop(i)
    else:
        mapp[i] = 1

value = max(list(mapp.keys())) if mapp else -1
print(value)
