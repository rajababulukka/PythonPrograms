class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

class BST(object):
    def inorderTraversal(self,root):
        result, current=[], root
        while current:
            if current.left is None:
                result.append(current.value)
                current = current.right
            else:
                node = current.left
                while node.right and node.right!=current:
                    node=node.right
                if node.right is None:
                    node.right=current
                    current=current.left
                else:
                    result.append(current.value)
                    node.right=None
                    current = current.right
        return result

if __name__ == "__main__":
    root = BinaryTreeNode(20)
    root.left = BinaryTreeNode(10)
    root.right = BinaryTreeNode(30)
    root.left.left = BinaryTreeNode(8)
    root.left.right = BinaryTreeNode(12)
    root.right.left = BinaryTreeNode(25)
    root.right.right = BinaryTreeNode(32)
    result = BST().inorderTraversal(root)
   
    
    print(result)
    print("Second largest is: ", result[-2])
