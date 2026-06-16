class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def insert_at_position(last, data, pos):
    if last == None:
        if pos != 1:
           return last
        
        new_node = Node(data)
        last = new_node
        last.next = new_node
        
        return last
    
    new_node = Node(data)

    #wskazuje na pierwszy element bo 
    # pozniej uzyjemy go do kierowania
    # sie do pozycji pos
    curr = last.next

    if pos == 1:
        new_node.next = curr
        last.next = new_node
        return last
    
    for i in range(1, pos - 1):
        curr = curr.next
        if curr == last.next:
            return last
        
    new_node.next = curr.next
    curr.next = new_node

    if curr == last:
        last = new_node
    return last

     
        