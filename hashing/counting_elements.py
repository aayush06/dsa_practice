"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
"""

arr = [1,2,3]
arr_set = set(arr)

count = sum(1 for i in arr if i+1 in arr_set)
print(count)
