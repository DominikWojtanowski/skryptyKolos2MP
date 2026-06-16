class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

# bedziemy wszystko implementowac jak w geeks for geeks
def search(root, key):
    if root is None:
        return None
    
    curr = root
    while curr is not None:
        if curr.data > key:
            curr = curr.left
        elif curr.data < key:
            curr = curr.right
        else:
            break
    return curr

def searchRecursion(root,key):
    if root is None:
        return False
    if root.data == key:
        return True
    
    if key > root.data:
        return searchRecursion(root.right,key)
    return searchRecursion(root.left, key)

def insert(root,key):

    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def insertIterative(root,key):
    temp = Node(key)
    if root is None:
        return temp
    
    curr = root
    while curr is not None:
        if curr.data > key and curr.left is not None:
            curr = curr.left
        elif curr.data < key and curr.right is not None:
            curr = curr.right
        else:
            break
    
    if curr.data > key:
        curr.left = temp
    else:
        curr.right = temp
    
    return root

def getSuccesor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def delNode(root, x):
    if root is None:
        return root
    
    if root.data > x:
        root.left = delNode(root,x)
    elif root.data < x:
        root.right = delNode(root,x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        succ = getSuccesor(root)
        root.data = succ.data
        root.right = delNode(root.right,succ.data)

    return root


        

            

        

        


            
