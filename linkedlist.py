class Node:
    data = None
    next_node = None


    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Node: {self.data}"

n1 = Node(10)
print(n1)
n1.next_node = 20
print(f"Next node of n1 is :{n1.next_node}")