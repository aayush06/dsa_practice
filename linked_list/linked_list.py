"""
    Collection of nodes
    head is used as reference to traverse linked list
    Complexity - 
    push - O(n)
    add node to start - O(1)
    print - O(n)
    length - O(n)
    middle element - O(n)
    sort - O(nlogn)
    reverse - O(n)
    remove duplicates - O(n)
"""


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        # if already empty add new node
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        # iterate over linked list
        while last.next:
            last = last.next
        # add new node to last
        last.next = new_node
        
    def add_node_to_start(self, data):
        # create new node with data
        new_node = Node(data)
        # if empty ll add new node
        if self.head is None:
            self.head = new_node
            return
        # add new node to start and point head to new node
        current_node = self.head
        self.head = new_node
        new_node.next = current_node
        
    def print_linked_list(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result = result + "->"+ str(current_node.data) if result else str(current_node.data)
            current_node = current_node.next
        print(result)
            
    def get_length_of_linked_list(self):
        count = 0
        current_node = self.head
        while current_node:
            count+=1
            current_node = current_node.next
        return count
    
    def get_middle_element(self):
        length = self.get_length_of_linked_list()
        if length<=1:
            return -1
        middle_index = length//2
        current_node = self.head
        count = 0
        while current_node:
            if count == middle_index:
                return current_node.data
            count += 1
            current_node = current_node.next
    
    def split(self, head):
        if not head or not head.next:
            return head, None
        
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        middle = slow_ptr.next
        slow_ptr.next = None
        return head, middle
    
    def merge(self, left_sorted, right_sorted):
        if not left_sorted and not right_sorted:
            return None
        if not left_sorted:
            return right_sorted
        if not right_sorted:
            return left_sorted
        if left_sorted.data <= right_sorted.data:
            result = left_sorted
            result.next = self.merge(left_sorted.next, right_sorted)
        else:
            result = right_sorted
            result.next = self.merge(left_sorted, right_sorted.next)
        return result
    
    def merge_sort(self, head):
        if not head or not head.next:
            return head
        left_half, right_half = self.split(head)
        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)
        
        return self.merge(left_sorted, right_sorted)

    def sort(self):
        self.head = self.merge_sort(self.head)
    
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
    def remove_duplicates(self):
        self.sort()
        head = self.head
        if not self.head or not self.head.next:
            return
        slow_ptr = self.head
        fast_ptr = self.head.next
        
        tmp_node = Node(0)

        while fast_ptr.next:
            
            if slow_ptr.data == fast_ptr.data:
                current_node = fast_ptr
                fast_ptr = fast_ptr.next
                current_node.next = None
                slow_ptr.next = fast_ptr
            else:
                slow_ptr = fast_ptr
                fast_ptr = fast_ptr.next
            
            

ll = LinkedList()
ll.push(2)
ll.push(3)
ll.push(4)
ll.print_linked_list()
length = ll.get_length_of_linked_list()
print("Length is %s"%length)
ll.add_node_to_start(1)
ll.print_linked_list()
length = ll.get_length_of_linked_list()
print("Length is %s"%length)
ll.push(7)
ll.print_linked_list()
middle_element = ll.get_middle_element()
print("Middle element %s"%middle_element)
ll.reverse()
ll.print_linked_list()
ll.push(10)
ll.add_node_to_start(20)
ll.print_linked_list()
ll.sort()
ll.print_linked_list()
ll.push(2)
ll.add_node_to_start(9)
ll.add_node_to_start(12)
ll.push(12)
ll.print_linked_list()
length = ll.get_length_of_linked_list()
print("Length is %s"%length)
ll.remove_duplicates()
ll.print_linked_list()
length = ll.get_length_of_linked_list()
print("Length is %s"%length)
