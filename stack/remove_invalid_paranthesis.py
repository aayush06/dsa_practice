"""
Given a string, s, that may have matched and unmatched parentheses, remove the minimum number of parentheses 
so that the resulting string represents a valid parenthesization. For example, the string “a(b)” represents 
a valid parenthesization while the string “a(b” doesn't, since the opening parenthesis doesn't have any 
corresponding closing parenthesis.

s[i] is either an opening parenthesis, a closing parenthesiss , or a lowercase English letter.
1 ≤ s.length ≤10^3

input - m)no(q)rs(
output - mno(q)rs

input - )()r(s(t(q(v)(w(x)y)z())((()(
output - ()rst(q(v)(w(x)y)z())()
"""

from stack import ArrayAsStack

def solution(s):
    stk = ArrayAsStack(len(s))
    for i,value in enumerate(s):
        if value==')':
            last_element = stk.peek()
            if last_element and last_element[0] == '(':
                stk.pop()
            if last_element and last_element[0] == ')':
                stk.push([value, i])
            if not last_element:
                stk.push([value, i])
        elif value == '(':
            stk.push([value, i])
    result = list(s)
    while stk.top:
        element = stk.pop()
        if element:
            result[element[1]] = ''
    return ''.join(result)

ans = solution(")()r(s(t(q(v)(w(x)y)z())((()(")
print(ans)
assert ans == '()rst(q(v)(w(x)y)z())()'
ans = solution("m)no(q)rs(")
print(ans)
assert ans == 'mno(q)rs'
        
