class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Stack class
class myStack:
    def __init__(self):
        
        # initially stack is empty
        self.top = None

    def push(self,x):
        v = Node(x)
        if self.top is None:
            self.top = v
            return
        v.next = self.top
        self.top = v


    def pop(self): 
        if self.top is None:
            print("underflow")
            return
        v = self.top
        self.top = self.top.next

        val = v.data
        del v
        return val