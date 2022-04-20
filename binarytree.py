class Node:
    def _init_(self,data):
        self.data = data
        self.left = left 
        self.right =right

#create two elemenst as children(left and right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

#if inorder
def  inorder(root):
    if not root:
        return
        print(root.data)
        inorder(root.left)
        inorder(root.right)
inorder(root)