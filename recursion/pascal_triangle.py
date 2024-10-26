"""
For given input return entire row corresponding to input from pascal triangle

pascal triangle - 
            1
           1  1
          1  2  1
        1   3  3  1
       1   4   6   4  1

Input - 3
Output - [1,3,3,1]
"""

def print_pascal(row):
    if row==0:
        return [1]
    else:
        r = [1]
        prev_row = print_pascal(row-1)
        for i in range(len(prev_row)-1):
            r.append(prev_row[i]+prev_row[i+1])
        r+=[1]
    return r

print(print_pascal(5))
