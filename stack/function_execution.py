"""
We are given an integer number, n, representing the number of functions running in a single-threaded CPU, and an execution log, 
which is essentially a list of strings. Each string has the format {function id}:{"start" | "end"}:{timestamp}, 
indicating that the function with function id either started or stopped execution at the time identified by the timestamp value. 
Each function has a unique ID between 0 and n-1. Compute the exclusive time of the functions in the program.

1<=n<=100
1<=logs.length<=500
0<=function_id<n
0<=timestamp<=10^3
No two start events and two end events will happen at the same timestamp.
Each function has an end log entry for each start log entry.

example - 
input - 
n=3
0:start:0 , 1:start:2, 1:end:3, 2:start:4, 2:end:7, 0:end:8

output - 
3 2 4

func 0 started - 0
func 1 started - 2
func 1 end - 3
func 2 start - 4
func 2 end - 7
func 0 end - 8

func 0 ran for 0,1,8 sec => 3
func 1 ran for 2,3 => 2
func 2 ran for 4,5,6,7 => 4
"""

from stack import ArrayAsStack

def solution(n, logs):
    stk = ArrayAsStack(len(logs))
    result = [0]*n
    for i in logs:
        parsed_log = i.split(':')
        last_element = stk.peek()
        if parsed_log[1] == 'start':
            stk.push(parsed_log)
        if parsed_log[1] == 'end':
            stk.pop()
            result[int(parsed_log[0])] += (int(parsed_log[2])-int(last_element[2])+1)
            if stk.peek():
                result[int(stk.peek()[0])] -= (int(parsed_log[2])-int(last_element[2])+1)
    return result   

logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
n = 1
print(solution(n, logs))

print("*"*50)

n=2
logs = ["0:start:0","1:start:3","1:end:6","0:end:10"]
print(solution(n, logs))

print("*"*50)
n=3 
logs = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]
print(solution(n, logs))
