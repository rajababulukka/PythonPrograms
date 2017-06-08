class BinaryTreeNode:

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

    def insert_left(self,value):
        
        self.left=BinaryTreeNode(value)
        print("left:",self.left)
        return self.left

    def insert_right(self,value):
        self.right=BinaryTreeNode(value)
        print("right:",self.right)
        return self.right

class Binary_or_not:

    def isValidBST(self, root):
        prev,current=None,root
        while current:
            if current.left is None:
                if prev and prev.value >= current.value:
                    return False
                prev = current
                current = current.right
            else:
                node=current.left
                while node.right and node.right!=current:
                    node=node.right
                if node.right is None:
                    node.right=current
                    current=current.left
                else:
                    if prev and prev.value >= current.value:
                        return False
                    node.right=None
                    prev=current
                    current=current.right
        return True
                    
                    
        

if __name__ == "__main__":
    
    b1 = BinaryTreeNode(1)
    b1.right=BinaryTreeNode(3)
    b1.left=BinaryTreeNode(2)
    result = Binary_or_not().isValidBST(b1)
    print(result)














