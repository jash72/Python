class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
def print_singleList(node):
    while node is not None:
        print(node.data, end = " ")
        node = node.next

head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third

print_singleList(head)
