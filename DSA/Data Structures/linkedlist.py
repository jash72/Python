class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class DoubleNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class CircularNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
