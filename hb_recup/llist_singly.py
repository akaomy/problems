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
        """ append new node with data to the end of list """
        new_node = Node(data)

        if not self.head:  # if False > if linkedList is empty > no node in it
            self.head = new_node

        if self.tail:  # if it has at least one item, non empty llist
            self.tail.next = new_node

        self.tail = new_node
        self.length = self.length + 1

    def traverse(self):
        """print out all data in each node"""
        while(self.head):
            print(self.head.data)
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

new_llist.traverse()
# can access only at the tail or head, or traverse trhough each item
# print(new_llist.head)
# print(new_llist.head.next)
# print(new_llist.tail)
# print(new_llist.length)
