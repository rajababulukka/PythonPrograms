class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        max=self.items[0]
        for i in range(1,len(self.items)):
            if self.items[i] > max:
                max=self.items[i]
        return max

if __name__=="__main__":

    s = Stack()
    s.push(2)
    s.push(4)    
    s.push(1)
    s.push(11)
    s.push(10)    
    s.pop()
    print(s.items)
    print(s.get_max())
    
    
                
                       
