"""
You are given an array arr[] of size n and multiple queries, where each query consists of two indices l and r.
For each query, return the sum of elements from index l to r (inclusive) in array.
Input - arr = [3, 8, 7, 10, 14]
        Queries: [(1, 3), (2, 4), (0, 2)]
Output - 
Sum from index 1 to 3: 25 (8 + 7 + 10)
Sum from index 2 to 4: 31 (7 + 10 + 14)
Sum from index 0 to 2: 18 (3 + 8 + 7)
"""

def calculate_sun_of_queries(arr, queries):
    result = [3]
    for i in range(1, len(arr)):
        result.append(result[i-1]+arr[i])
    for i in queries:
        if i[0] == 0:
            print(result[i[1]])
        else:
            print(result[i[1]]-result[i[0]-1])


arr = [3, 8, 7, 10, 14]
queries = [(1, 3), (2, 4), (0, 2)]
calculate_sun_of_queries(arr, queries)
