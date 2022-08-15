class Node:

    def __init__(self, node_data):
        self.data = node_data
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
        """ append new node with data to the end of list """
        new_node = Node(data)

        if not self.head:  # if False > if linkedList is empty > no node in it
            self.head = new_node

        if self.tail:  # if it has at least one item, non empty llist
            self.tail.next = new_node

        self.tail = new_node
        self.length = self.length + 1

    def add_at_head(self, data):
        """add a node at the beginning"""

        current = Node(data)
        current.next = self.head
        self.head = current
        self.length = self.length + 1

    def traverse(self):
        """print out all data in each node"""
        while(self.head):
            print('t', self.head.data)
            self.head = self.head.next

    def search(self, item):
        while(self.head):
            # problem to compare <class '__main__.Node'> <class 'int'>
            # print('41 self.head.data item', type(self.head.data), type(item))
            if self.head.data == item:
                # return True
                print('44 self.head.data item', self.head.data, item)
            self.head = self.head.next

    # TODO: finish this funciton
    def pop(self):
        """delete node from the end of linked list"""
        while(self.head):
            if self.head == None:
                return None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

new_llist = LinkedList()

new_llist.append(node1)
new_llist.append(node2)
new_llist.append(node3)

# can access only at the tail or head, or traverse trhough each item

print(new_llist.add_at_head(100))
print(new_llist.add_at_head(120))
print(new_llist.traverse())
print(new_llist.length)
