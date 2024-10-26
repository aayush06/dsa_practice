"""
You are given a string consisting of lowercase English letters. Repeatedly remove adjacent duplicate letters,
one pair at a time. Both members of a pair of adjacent duplicate letters need to be removed.
1<=len(s)<10^3
string consists of lowercase English alphabets.
Input - aaa
output - a

input - abbaaca
output - aca

input - sadkkdassa
output - sa
"""
from stack import ArrayAsStack

def remove_duplicates(s):
    stk = ArrayAsStack(len(s))
    for i in s:
        last_element = stk.peek()
        if last_element == i:
            stk.pop()
        else:
            stk.push(i)
    solution = []
    while stk.top:
        solution.append(stk.pop())
    solution.reverse()
    return ''.join(solution)

s = "sadkkdassa"
print(remove_duplicates(s))

s = "abbaaca"
print(remove_duplicates(s))

s = "aaa"
print(remove_duplicates(s))
