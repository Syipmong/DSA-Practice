class Queeue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        """Add an element to the end of the queue"""
        self.item = item
        self.items.append(self.item)
        

    def dequeue(self):
        """Remove and return the first item in the queue"""
        if len(self.items) != 0:
            self.items.pop(-1)
        return f"List is empty"
    
    def size(self):
        """Return the number of items in the queue"""
        self.count = 0
        while self.item != 0:
            return len(self.items)
        return f"Queue is empty"
    
    def is_empty(self):
        """Check if the queue is empty or not"""
        return len(self.items) == 0
    
    def display(self):
        """Print all elements in the queue"""
        return self.items

   

q = Queeue()
q.enqueue(10)
q.enqueue(15)
q.enqueue(11)
q.enqueue(100)
q.enqueue(7)
print(q.display())
print(q.size())
q.dequeue()
q.dequeue()
print(q.display())
q.dequeue()
print(q.display())
print(q.size())
print(q.is_empty())