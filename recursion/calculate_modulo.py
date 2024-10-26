"""
Calculate modulo of given dividend and divisor
"""

def mod(dividend, divisor) :
  if divisor == 0 :
    print("Divisor cannot be ")
    return 0
  if dividend < divisor :
    return dividend
  else :
    return mod(dividend - divisor, divisor)

print(mod(10, 4))
