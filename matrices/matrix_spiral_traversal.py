"""
Given an mxn matrix, return an array containing the matrix elements in spiral order,
starting from the top-left cell.

Input - matrix = [[7, 1, 7, 5],[8, 9, 7, 9],[4, 4, 7, 3]]
Output - [7, 1, 7, 5, 9, 3, 7, 4, 4, 8, 9, 7]
"""

def matrix_spiral_traversal(matrix):
    direction = 1 # 1 for left to right and top to bottom scan, -1 for right to left and bottom to up scan
    row, rows, col, cols = 0, len(matrix), -1, len(matrix[0])
    traverse = []
    while rows > 0 and cols > 0:
        for _ in range(cols):
            col+=direction
            traverse.append(matrix[row][col])
        rows -= 1

        for _ in range(rows):
            row+=direction
            traverse.append(matrix[row][col])
        cols -=1
        
        direction*=-1 # to reverse direction
    
    return traverse

matrix = [[7, 1, 7, 5],[8, 9, 7, 9],[4, 4, 7, 3]]
print(matrix_spiral_traversal(matrix))

matrix = [[3,1,1],[15,12,13],[4,14,12],[10,5,11]]
print(matrix_spiral_traversal(matrix))
            