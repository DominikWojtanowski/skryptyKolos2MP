class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# sposob konwertowanie na tablice
def countNodes(head):
    count = 0
    tmp = head

    while tmp is not None:
        count += 1
        tmp = tmp.next

    return count

def convertToArr(head,arr,count):
    curr = head
    for i in range(count):
        arr[i] = curr.data
        curr = curr.next
    

def changeHalf(arr,n ):
    for i in range(n // 2):
        x = arr[i]
        arr[i] = arr[n - i - 1] - x
        arr[n - i - 1] = x
    

def convertToList(arr,head, n):
    tmp = head
    for i in range(n):
        tmp.data = arr[i]
        tmp = tmp.next


def reverseList(head):
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
def modifyList(head):
    
    if head.next == None:
        return head
    
    slow = head
    fast = head

    while slow.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow
    reverse_list = mid.next
    mid.next = None

    reverse_list = reverseList(reverse_list)

    curr1 = head
    curr2 = reverse_list

    while curr2 is not None:
        x = curr1.data
        curr1.data = curr2.data - x
        curr2.data = x
        curr1 = curr1.next
        curr2 = curr2.next
    
    mid.next = reverseList(reverse_list)

def reverseListRecursion(head):
    if head is None or head.next is None:
        return head
    rest = reverseList(head.next)

    # zeby nam element za head wskazywal na
    # head czzyli
    # kiedy mamy 1 -> 2 -> 3 -> 4
    # to zeby 4 -> 3 i 3 -> 2 itd
    head.next.next = head

    # teraz obecny element jest naszym
    # koncem tabeli
    head.next = None

    return rest

def reverseStack(head):
    
    stack = []
    temp = head
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next

    head = temp
    while stack:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None
    return head



    





