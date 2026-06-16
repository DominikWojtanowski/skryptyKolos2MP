class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def postorder(root,res):
    if root is None:
        return 
    
    postorder(root.left, res)
    postorder(root.right,res)
    res.append(root.data)

    

def postorderIterative(root):
    res = []
    if root is None:
        return res
    
    stk1 = []
    stk2 = []
    stk1.append(root)
    while stk1:
        curr = stk1.pop()
        stk2.append(curr)

        if curr.left:
            stk1.append(curr.left)
        if curr.right:
            stk1.append(curr.right)

    while stk2:
        curr = stk2.pop()
        res.append(curr.data)

    return res


    

    