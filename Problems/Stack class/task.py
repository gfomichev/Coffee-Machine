class Stack:

    def __init__(self):
        self.stack = []

    def push(self, _el):
        self.stack.append(_el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
