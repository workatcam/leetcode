class Queue:
    def __init__(self):
        self.value = []
    def push(self, x):
        self.value.append(x)
    def pop(self):
        return self.value.pop(0)
    def top(self):e
        return self.value[0]
    def size(self):
        return len(self.value)

class MyStack:

    def __init__(self):
        self.emptyQueue = Queue()
        self.valueQueue = Queue()

    def push(self, x):
        self.valueQueue.push(x)
        
    def pop(self) -> int:

        while self.valueQueue.size() >=2:
            self.emptyQueue.push(self.valueQueue.pop())
            
        if self.valueQueue.size() == 1:
            popvalue = self.valueQueue.pop()

        self.emptyQueue, self.valueQueue = self.valueQueue, self.emptyQueue

        return popvalue
        
    def top(self) -> int:
        
        while self.valueQueue.size() >=2:
            self.emptyQueue.push(self.valueQueue.pop())
            
        if self.valueQueue.size() == 1:
            popvalue = self.valueQueue.pop()
            self.emptyQueue.push(popvalue)

        self.emptyQueue, self.valueQueue = self.valueQueue, self.emptyQueue

        return popvalue

    def empty(self) -> bool:
        return self.valueQueue.size() == 0
