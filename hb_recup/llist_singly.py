class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        print(f"<Node object. Data: {self.data}, Next node: {self.next}")


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        """ creates new node with passed data into it and assigns it to head and tail """
        new_node = Node(data)

        if not self.head:  # if False > if linkedList is empty > no node in it
            self.head = new_node

        if self.tail:  # if it has at least one item, non empty llist
            self.tail = new_node

        self.tail = new_node


new_llist = LinkedList()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

new_llist.append(node1)
new_llist.append(node2)
new_llist.append(node3)

# can access only at the tail or head, or traverse trhough each item
print(new_llist.head)
print(new_llist.tail)
