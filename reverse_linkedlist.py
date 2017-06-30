class Node:
    def __init__(self, data):
        self.data = data
        self.next  = None
        
class LinkedListNode:

    def __init__(self):
        self.head = None

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def insert(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    
        
a = LinkedListNode()
a.insert(5)
a.insert(9)
a.insert(1)

a.print_list()
a.reverse_linked_list()
print("after reverse")
a.print_list()
