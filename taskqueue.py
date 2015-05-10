from collections import deque

class TaskQueue:

    def __init__(self):
        self.deque = deque()
        self.size = 0

    def push(self, task):
        self.deque.append(task)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.deque.popleft()
        else:
            return None

    def peek_all(self):
        return [element for element in self.deque]

    def peek_next(self):
        val = self.pop()
        if val:
            self.deque.appendleft(val)
            self.size += 1
        return val

    def count(self):
        return self.size