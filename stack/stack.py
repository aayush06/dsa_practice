"""
- LIFO based data structure
- operations - push (add element to top of stack) & pop (remove element from top of stack)
- reference using top
- overflow and underflow conditions
- Complexities - 
    push - O(1)
    pop - O(1)
    peek - O(1) - get last element with removing
    isEmpty - O(1)
    size - O(1)
- Used generally in below scenarios - 
  Reverse order processing: The problem involves processing elements in reverse order or requires the last element added to be processed first.
  Nested structures handling: The problem involves nested structures, like parentheses, brackets, or nested function calls.
  State tracking: The problem requires keeping track of previous states or undoing operations.
  Expression evaluation: The problem involves evaluating expressions.
"""

class ArrayAsStack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = 0
        
    def push(self, data):
        if self.top == self.size:
            print("Overflow condition")
            return None
        self.stack.append(data)
        self.top += 1
        
    def pop(self):
        if self.isEmpty():
            print("Underflow condition")
            return None
        item = self.stack[self.top-1]
        self.stack.pop(self.top-1)
        self.top-=1
        return item
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.top-1]
    
    def isEmpty(self):
        if self.top==0:
            return True
        return False
    
    def get_size(self):
        return self.top


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListAsStack:
    def __init__(self, size):
        self.head = None
        self.size = size
        self.top = 0
        
    def push(self, data):
        node = Node(data)
        if self.top == self.size:
            print("Overflow condition")
            return -1
        self.top += 1
        if not self.head:
            self.head = node
            return
        current_node = self.head
        self.head = node
        node.next = current_node
    
    def pop(self):
        if self.top == 0 or not self.head:
            print("Under flow condition")
            return -1
        node = self.head
        self.head = node.next
        self.top-=1
        return node.data
        
    def print_linked_list(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result = result + "->"+ str(current_node.data) if result else str(current_node.data)
            current_node = current_node.next
        print(result)
    
# stack = ArrayAsStack(3)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.pop()
# print(stack.get_size())
# print(stack.peek())
# stack.pop()
# stack.pop()
# stack.pop()
# print("*"*40)
# stack_ll = LinkedListAsStack(3)
# stack_ll.push(1)
# stack_ll.push(2)
# stack_ll.push(3)
# stack_ll.push(4)
# stack_ll.print_linked_list()
# print(stack_ll.pop())
# print(stack_ll.pop())
# print(stack_ll.pop())
# print(stack_ll.pop())
