"""
Given a matrix, mat, if any element within the matrix is zero, set that row and column to zero.
Constraints:
1≤mat.row, mat.col ≤20
-2^31 ≤ mat[i][j] ≤ (2^31)-1

input - [[1,2,3],[4,5,6],[7,0,9]]
output - [[1,0,3],[4,0,6],[0,0,0]]

input - [[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1]]
output - [[0,0,0,0,0],[1,0,0,1,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,1,1]]
"""

def set_zeroes(arr):
    zero_row_index = set()
    zero_column_index = set()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                zero_row_index.add(i)
                zero_column_index.add(j)
    for i in zero_row_index:
        for j in range(len(arr[0])):
            arr[i][j] = 0
    
    for j in zero_column_index:
        for i in range(len(arr)):
            arr[i][j] = 0
    return arr

def set_zeroes_optimised_space(mat):
    rows = len(mat)
    cols = len(mat[0])
    fcol = False
    frow = False

    for i in range(rows):
        if mat[i][0] == 0:
            fcol = True

    for i in range(cols):
        if mat[0][i] == 0:
            frow = True

    for i in range(1, rows):
        for j in range(1, cols):
            if mat[i][j] == 0:
                mat[0][j] = mat[i][0] = 0

    for i in range(1, rows):
        if mat[i][0] == 0:
            for j in range(1, cols):
                mat[i][j] = 0

    for j in range(1, cols):
        if mat[0][j] == 0:
            for i in range(1, rows):
                mat[i][j] = 0

    if fcol:
        for i in range(rows):
            mat[i][0] = 0

    if frow:
        for j in range(cols):
            mat[0][j] = 0
    return mat

arr = [[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1]]
# print(set_zeroes(arr))
print(set_zeroes_optimised_space(arr))


