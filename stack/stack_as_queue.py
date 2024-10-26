"""
Design a custom queue, MyQueue, using only two stacks. Implement the Push(), Pop(), Peek(), and Empty() methods:

Void Push(int x): Pushes element to the back of the queue.
Int Pop(): Removes and returns the element from the front of the queue.
Int Peek(): Returns the element at the front of the queue.
Boolean Empty(): Returns TRUE if the queue is empty. Otherwise FALSE.
You are required to only use the standard stack operations, which means that only the Push() to top,
Peek() and Pop() from the top, Size(), and Is Empty() operations are valid.
"""


class Queue:
    def __init__(self) -> None:
        self.stk_1 = []
        self.stk_2 = []
        
    def enqueue(self, data):
        if self.stk_1:
            while self.stk_1:
               self.stk_2.append(self.stk_1.pop())
        self.stk_1.append(data)
        while self.stk_2:
            self.stk_1.append(self.stk_2.pop())
        return None
        
    def dequeue(self):
        return self.stk_1.pop()
    
    def peek(self):
        return self.stk_1[-1]
        
    def empty(self):
        if not self.stk_1:
            return True
        return False
    
queue = Queue()
print(queue.enqueue(9))
print(queue.enqueue(3))
print(queue.enqueue(1))
print(queue.dequeue())
print(queue.peek())
print(queue.empty())
