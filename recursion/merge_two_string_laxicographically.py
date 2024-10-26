"""
Lexicographical means that something is organized according to alphabetical order.

Input string 1 - acu
      string 2 - bst

Output - abcust
"""

def merge(string1, string2) :
  if string1 == "" :
    if string2 == "" : 
      return ""
    return string2

  elif string2 == "" :
    return string1

  elif string1[0] > string2[0] :
      return string2[0] + merge(string1, string2[1:])

  return string1[0] + merge(string1[1:], string2)


string1 = "acu"
string2 = "bst"
print(merge(string1, string2))
