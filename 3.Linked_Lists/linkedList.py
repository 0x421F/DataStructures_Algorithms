#Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

firstNode = Node("John")
secondNode = Node("Ben")
thirdNode = Node("Mathew")

firstNode.next = secondNode
secondNode.next = thirdNode

print(firstNode.data)
print(firstNode.next.data)


#Doubly Linked List

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

firstNode = DoublyNode("John")
secondNode = DoublyNode("Ben")
thirdNode = DoublyNode("Mathew")

firstNode.next = secondNode
secondNode.next = thirdNode
secondNode.prev = firstNode
thirdNode.prev = secondNode

print(firstNode.data)
print(firstNode.next.data)
print(secondNode.prev.data)
print(thirdNode.prev.data)