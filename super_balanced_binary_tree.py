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

class binary:
    
    def isBalanced(self,root):
        return self.isBalancedInt(root)>=0

    
    def isBalancedInt(self,root):
        if (root==None):
            return 0

        left = self.isBalancedInt(root.left)
        right = self.isBalancedInt(root.right)

        if left<0 or right <0 or abs(left-right)>1:
            return -1

        return max(left,right)+1

if __name__ == "__main__":
    b1 = BinaryTreeNode(0)
    b1.left=BinaryTreeNode(1)
    b1.right=BinaryTreeNode(2)
    b1.left.left=BinaryTreeNode(3)
    b1.left.left=BinaryTreeNode(4)
    b1.right.left=BinaryTreeNode(5)
    b1.right.right=BinaryTreeNode(6)
    b1.left.left.right=BinaryTreeNode(1)
    b1.left.left.right.right=BinaryTreeNode(4)
    #b1.left.left=BinaryTreeNode(60)
    #b1.left.left=BinaryTreeNode(70)
    #b1.left.left=BinaryTreeNode(80)
    
    print(binary().isBalanced(b1))


