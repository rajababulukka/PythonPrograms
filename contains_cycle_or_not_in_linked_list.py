class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

    def contains_cycle(node):
        s = node
        while node.next and node.next.next:
            print("%s->%s",(node.value,node.next))
            s = s.next
            node = node.next.next
            if node is s:
                return True
        return False
        
a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)

a.next = b
b.next = c
c.next = a

print(LinkedListNode.contains_cycle(a))
