"""
A 2D array m*n
m - rows, n - columns
addititon/substraction - element wise
multiplication - addition of multiplication of each element of matrix 1 row with matrix 2 column
inverse - B is inverse of A if AB = BA = I, denoted by A^-1
transpose - interchange of rows with columns
scalar multiplication - constant k multiplied by each element 
rotation - matrix rotated clockwise/anti-clockwise by some degree
reflection - elements flipped over some axis

traversal -
    [[1,2,3],[4,5,6],[7,8,9]]
    row major - traverse entire first row then second row and so on 1->2->3->4->5->6->7->8->9
    column major - traverse entire first column then second column and so on 1->4->7->2->5->8->3->6->9
    diagnol traversal - top-left to bottom right or bottom-right to top left 1->2->4->7->5->3->6->8->9
    spiral traversal - otermost to center 1->2->3->6->9->8->7->4->5
    
Toeplitz matrix - if every descending diagonal from left to right (or basically every left diagonal) has the same elements.
A = [[5,9,4,1],[2,5,9,4],[3,2,5,9]]
A[1][1] == A[0][0] && A[1][2]==A[0][1] && A[1][3]==A[0][2]
A[2][1]==A[1][0] && A[2][2]==A[1][1] && A[2][3]==A[1][2]
"""
