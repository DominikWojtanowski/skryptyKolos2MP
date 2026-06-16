class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def levelorder(root,level,res):
    if root is None:
        return root
    
    if len(res) <= level:
        res.append([])
    
    res[level].append(root.data)
    
    levelorder(root.left,level + 1, res)
    levelorder(root.right,level + 1, res)




def levelorderIteratywny(root):
    if root is None:
        return []
    
    q = []
    res = []
    curr_level = 0

    q.append(root)
    while q:
        res.append([])
        len_q = len(q)
        for i in range(len_q):
            curr = q.pop(0)
            res[curr_level].append(curr.data)
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        curr_level+=1
    return res
    