"""
Given an n*n matrix, rotate the matrix 90 degrees clockwise. The performed rotation should be in place, i.e.,
the given matrix is modified directly without allocating another matrix.
"""


def rotate_matrix(matrix):
  n = len(matrix)
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
  for i in range(n):
    for j in range(n // 2):
      matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
  return matrix

matrix = [[3,1,1,7],[15,12,13,13],[4,14,12,4],[10,5,11,12]]
print(rotate_matrix(matrix))
