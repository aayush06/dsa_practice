"""
Implement a function that takes two numbers, testVariable1 and testVariable2 and returns their greatest common divisor.

Input
Two variables testVariable1 and testVariable2 containing numbers.

Output
The greatest common divisor of testVariable1 and testVariable2.

Sample Input
6, 9

Sample Output
3
"""

def gcd(testVariable1, testVariable2) :
  if testVariable1 == testVariable2 :
    return testVariable1

  if testVariable1 > testVariable2 :
    return gcd(testVariable1 - testVariable2, testVariable2)
  else :
    return gcd(testVariable1, testVariable2 - testVariable1)

number1 = 6
number2 = 9
print(gcd(number1, number2))
