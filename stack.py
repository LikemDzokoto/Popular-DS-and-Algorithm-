from collections import deque

class Stack:
    def __init__(self, ):
        # I might add functionality to allow conversion of a list to a stack by adding it's
        # items upon creation.
        self.stack = deque()

    def add(self, item):
        return self.stack.appendleft(item)

    def remove(self, item):
        return self.stack.pop(item)

    def show(self):
        for item in self.stack:
            yield(item)