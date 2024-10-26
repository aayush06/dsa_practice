"""
Implement a function that takes a variable, testVariable, and finds the number 
that is placed at that index in the Fibonacci sequence.

Input
A testVariable that contains the index whose corresponding element in the Fibonacci sequence will be found.

Output
The corresponding element in the Fibonacci sequence.

Sample Input
7
Sample Output
13
"""

def fibonnaci(index):
    if index<=1:
        return index
    else:
        return fibonnaci(index-1)+fibonnaci(index-2)

print(fibonnaci(7))
