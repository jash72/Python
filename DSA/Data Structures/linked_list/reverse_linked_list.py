class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def reversed_linked_list(head):
    curr = head
    prev = None
    
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev

def print_linked_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()
        
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth  = Node(5)
sixth = Node(6)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print_linked_list(head)
head = reversed_linked_list(head)
print_linked_list(head)