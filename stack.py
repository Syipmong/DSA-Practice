class Stack:
    """A simple implementation of a stack"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Pushes an element to the stack"""
        self.items.append(item)

    def pop(self):
        """Pops an element from the stack"""
        return self.items.pop()
    
    def peek(self):
        """Returns the top element of the stack"""
        return self.items[-1]
    


s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.push(7)
s1.push(8)
s1.push(9)
s1.push(10)
print(s1.items)
s1.pop()
s1.pop()

print(s1.items)
