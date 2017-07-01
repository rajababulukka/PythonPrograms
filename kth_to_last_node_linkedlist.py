class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

    def kth_to_last_node(k,head):
        i=0
        kth = head
        while(head and head.next):
            head = head.next
            if i==k-1:
                kth = kth.next
            else:
                i+=1
        return kth.value


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e
print(LinkedListNode.kth_to_last_node(2, a))

