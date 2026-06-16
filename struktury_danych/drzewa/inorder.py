class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def inorder(root,res):
    if root is None:
        return 
    
    inorder(root.left, res)
    res.append(root)
    inorder(root.right,res)

def inorderIteratywny(root):
    ans = []
    stack = []

    curr = root
    while curr is not None or len(stack) > 0:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        ans.append(curr.data)
        curr = curr.right
    return ans