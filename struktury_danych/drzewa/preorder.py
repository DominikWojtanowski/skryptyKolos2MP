class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def preorder(root,res):
    if root is None:
        return 
    
    res.append(root.data)
    preorder(root.left, res)
    preorder(root.right, res)

def preorderIterative(root):
    res = []
    stack = [root]

    while stack:
        curr = stack.pop()
        res.append(curr.data)

        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    return res

    