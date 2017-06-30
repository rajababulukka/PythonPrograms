class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

    def delete_node(node):
        tmp_ptr = node.next
        print("tmp_ptr",tmp_ptr)
        if tmp_ptr:
            node.next = tmp_ptr.next
            print("node.next",node.next)
            node.value = tmp_ptr.value
            print("node.value",node.value)
        else:
            raise ValueError("Can't delete value")

    

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

LinkedListNode.delete_node(b)


