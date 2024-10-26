"""
You have n balls and a 2D grid of size m*n representing a box. The box is open on the top and bottom sides.
Each cell in the box has a diagonal that can redirect a ball to the right or the left. You must drop 
n balls at each column's top. The goal is to determine whether each ball will fall out of the bottom or 
become stuck in the box. Each cell in the grid has a value of 1 or -1
1 - represents that the grid will redirect the ball to the right.
-1 - represents that the grid will redirect the ball to the left.
A ball gets stuck if it hits a V-shaped pattern between two grids or if a grid redirects the ball into either wall of the box.

The solution should return an array of size n with the ith element indicating the column that the ball falls out of, or it becomes 
-1 if it's stuck. If the ball drops from column x and falls out from column y then in the result array, index x contains value y.
"""
def ball_fall(matrix):
    result = [-1]*len(matrix[0])
    rows = len(matrix)
    cols = len(matrix[0])
    for col in range(cols):
        current_col = col
        for row in range(rows):
            next_col = current_col+matrix[row][current_col]
            if next_col<0 or next_col>len(matrix[0])-1 or matrix[row][current_col]!=matrix[row][next_col]:
                break
            if row==len(matrix)-1:
                result[col]=next_col
            current_col=next_col
    return result
            
        
    