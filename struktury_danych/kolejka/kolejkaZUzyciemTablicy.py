#Enqueue (insertion) 	O(1)
#Deque (deletion)   	O(n)
#Front (Get front)   	O(1)
#Rear (Get Rear)	O(1)
#IsFull (Check queue is full or not)	O(1)
#IsEmpty (Check queue is empty or not)	O(1)
class Queue:
    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.capacity = capacity
        self.size = 0
    def enqueue(self,x):
        if self.size == self.capacity:
            print("Overflow")
            return
        
        self.queue[self.size] = x
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            print("Underflow")
            return
        
        for i in range(1, self.size):
            self.queue[i-1] = self.queue[i]
        
        self.size -= 1

    def front(self):
        if self.size > 0:
            return self.queue[0]
    
    def rear(self):
        if self.size > 0:
            return self.queue[self.size-1]
        
class Queue2:
    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
    def enqueue(self, x):
        if self.size == self.capacity:
            print("Overflow")
            return
        
        idx = (self.front + self.size) % self.capacity
        self.queue[idx] = x
        self.size += 1
    def deque(self):
        if self.size == 0:
            print("Underflow")
            return
        
        v = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return v

        
    

    
        



