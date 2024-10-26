"""
Given a string containing an arithmetic expression, implement a basic calculator that evaluates the expression string.
The expression string can contain integer numeric values and should be able to handle the “+” and “-” operators, as well as “()” parentheses.
Let s be the expression string. We can assume the following constraints:
    1<=s.len<=3*10^3
    s consists of digits, “+”, “-”, “(”, and “)”
    s represents a valid expression.
    + is not used as unary operation eg (+1 and +(2+3) are invalid)
    - can be used as unary operation eg (-1 and -(2+3) are valid)
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
    
ex - (8 + 100) + (13 - 8 - (2 + 1))
o/p - 110
"""

from stack import ArrayAsStack

def simple_calculator(s):
    stack = ArrayAsStack(len(s))
    signed = 1
    number = 0
    result = 0
    second_number = 0
    for i in s:
        if i.isdigit():
            number = number*10+int(i)
        elif i == '+' or i == '-':
            result += number*signed
            if i == '+':
                signed = 1
            else:
                signed = -1
            number=0
        elif i == '(':
            stack.push(result)
            stack.push(signed)
            result = 0
            signed = 1
        elif i == ')':
            result += number*signed
            sign_value = stack.pop()
            result = sign_value*result
            second_number = stack.pop()
            result += second_number
            number = 0
    return result+number*signed
    

solution = simple_calculator("4 + (52 - 12) + 99")
print(solution)
solution = simple_calculator("(31 + 7) - (5 - 2)")
print(solution)
solution = simple_calculator("(12 - 9 + 4) + (7 - 5)")
print(solution)
solution = simple_calculator("8 - 5 + (19 - 11) + 6 + (10 + 3)")
print(solution)
solution = simple_calculator("56 - 44 - (27 - 17 - 1) + 7")
print(solution)
