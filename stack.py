class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Pushes an element to the stack"""
        self.items.append(item)

    def pop(self):
        """Pops an element from the stack"""
        return self.items.pop()