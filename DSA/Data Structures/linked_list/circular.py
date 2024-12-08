class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
    
def print_circularlinkedlist(node):
    pass

head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third
third.next = head
    
    