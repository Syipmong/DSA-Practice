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
            self.items.pop(0)
        return f"List is empty"
    
    def size(self):
        """Return the number of items in the queue"""
        self.count = 0
        for i in self.items:
            self.count +=1
            return self.count
        return f"Queue is empty"
    
    def is_empty(self):
        """Check if the queue is empty or not"""
        return len(self.items) == 0
    
    def display(self):
        """Print all elements in the queue"""

   

q = Queeue()
q.enqueue(10)
q.enqueue(15)
q.enqueue(7)
q.dequeue()
q.dequeue()
q.dequeue()
print(q.size())
print(q.is_empty())