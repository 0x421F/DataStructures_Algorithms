class queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
myQueue = queue()
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
print(myQueue.size())
print(myQueue.dequeue())
print(myQueue.dequeue())
