"""
Given a string that may consist of opening and closing parentheses, your task is to check whether or not
the string contains valid parenthesization.
The conditions to validate are as follows:
Every opening parenthesis should be closed by the same kind of parenthesis. Therefore, {)and [(]) strings are invalid.
Every opening parenthesis must be closed in the correct order. Therefore, )( and ()(() are invalid.

Input - (){[{()}]}
Output - True

Input - ))){{}}}]]
Output - False

"""

def is_valid(s):
    stk = []
    bracket_map = {')':'(', '}':'{', ']':'['}
    for i in s:
        if i in bracket_map.values():
            stk.append(i)
        elif i in bracket_map.keys() and stk:
            last_element = stk.pop()
            if last_element ==  bracket_map[i]:
                continue
            else:
                return False
        else:
            return False
    return True if not stk else False

s = '(){[{()}]}'
print(is_valid(s))
