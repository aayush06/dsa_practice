"""
Calculate power of given input number using exponent
"""

def power(n, exp):
    if exp==0:
        return 1
    else:
        return n*power(n, exp-1)

print(power(3,2))
