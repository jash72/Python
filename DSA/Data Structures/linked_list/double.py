class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

def forward_traversal(head):
    curr = head
    while curr is not None:
        print(curr.data, end= " ")
        curr = curr.next
    print()

def backward_traversal(tail):
    curr = tail
    while curr is not None:
        print(curr.data,end=" ")
        curr = curr.prev
    print()
        
        

head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.prev = head
second.next = third
third.prev = second

forward_traversal(head)
backward_traversal(third)