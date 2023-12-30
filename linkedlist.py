class Node:
    """Implementation for the Node"""
    data = None
    next_node = None


    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node: {self.data}"


class LinkedList:
    """Implementation for the LinkedList"""
    def __init__(self):
        self.head = None


    def __repr__(self):
        """Return a string representation of the list."""
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node
        return '-> '.join(nodes)
    

    def search(self,value):
        """Search the linked list for a node with the requested value and return the node."""
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next_node
        return None

    def is_empty(self):
        """Return True if the list is empty."""
        return self.head == None

    def size(self):
        """Return the number of nodes in the list."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
         
    def add(self,data):
        """Add a new node at the head of the list."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        return self.head

    






l = LinkedList()

l.add(20)
l.add(10)
l.add(22)
l.add(90)
print(l.size())
print(l)

print(l.search(22))
print(l.search(100))