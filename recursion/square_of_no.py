"""
Implement a function that takes a specific number testVariable and returns the square of the number.

Remember to implement your solution recursively.

Input
A variable testVariable that contains the input number

Output
The square of the input number

Sample Input
5
Sample Output
25
"""

def findSquare(targetNumber) :
  if targetNumber == 0 :
    return 0
  else :
    return findSquare(targetNumber - 1) + (2 * targetNumber) - 1

targetNumber = 5
print(findSquare(targetNumber))
