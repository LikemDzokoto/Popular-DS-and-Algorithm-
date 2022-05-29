from collections import deque

class Queue:
    def __init__(self, ):
        self.queue = deque()
        self.length = len(self.queue)

    def update(self, ):
        try:
            self.head = self.queue[0]
            self.tail = self.queue[-1]
        except (IndexError):
            self.head = None
            self.tail = None
        finally:
            return()
    
    def enqueue(self, item):
        self.queue.extend(item)
        self.update()
        return self.queue
    
    def dequeue(self, ):
        self.queue.popleft()
        self.update()
        return self.queue
    
    def show(self, ):
        for item in self.queue:
            print(item)