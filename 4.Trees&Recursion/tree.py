class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        newNode = Node(value)

        if self.root is None:

            self.root = newNode
            return True

        tempNode = self.root

        while True:

            if newNode.value == tempNode.value:
                return False

            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left

            else:
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, value):
        tempNode = self.root

        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False

    def minOfNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def maxOfNode(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode


myTree = BinarySearchTree()
myTree.insert(10)
myTree.insert(10)
myTree.insert(8)
myTree.insert(20)
myTree.insert(25)
myTree.insert(16)
myTree.contains(16)
myTree.contains(10)
myTree.contains(19)
myTree.root.value
myTree.root.right.value
myTree.root.right.right.value
myTree.root.left.value
myTree.minOfNode(myTree.root).value
myTree.maxOfNode(myTree.root).value

