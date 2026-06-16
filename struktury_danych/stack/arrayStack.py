class myStack:

    def __init__(self, cap):
        
        # array to store elements
        self.arr = [0] * cap
        
        # maximum size of stack
        self.capacity = cap
        
        # index of top element
        self.top = -1

    def push(self,x):
        if self.top == self.capacity - 1:
            print("Overflow")
            return
        
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            print("underflow")
            return
        
        x = self.arr[self.top]
        self.top -= 1
        return x

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return -1
        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1
    
    