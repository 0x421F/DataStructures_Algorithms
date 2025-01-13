class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addLeft(self, item):
        self.items.insert(item)
    
    def addRight(self, item):
        self.items.append(item)

    def removeLeft(self):
        return self.items.pop(0)
    
    def removeRight(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
myDeque = Deque()
print(myDeque.isEmpty())
myDeque.addRight(4)
myDeque.addRight('dog')
myDeque.addLeft('cat')
myDeque.addLeft(8)
print(myDeque.size())
print(myDeque.isEmpty())
