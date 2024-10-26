"""
Convert decimal to binary and print string of corresponding binary

Input - 
11

Output -
1011
"""

def get_binary(n):
    if n<=1:
        return str(n)
    else:
        remainder = n%2
        quotient = n//2
        return get_binary(quotient)+get_binary(remainder)

print(get_binary(11))
