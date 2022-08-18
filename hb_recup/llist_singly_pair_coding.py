# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# delete from beginning and from the end


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        print(f"Node [data {self.data} | next {self.next} ]")


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self):
        while(self.head):
            print(self.head.data)
            self.head = self.head.next

    def add_at_the_end(self, data):

        # LL
        # self.head = None
        # self.tail = None
        # self.size = 0

        # []

        # Node1 [data | next ]
        # Node2 [data | next ]
        # Node3 [data | next ]

        # Node [data | next] -> Node [data | next] -> Node [data | next] -> X

        # create a node
        new_node = Node(data)

        # check if ll is empty
        # we assign new node to head
        if not self.head:
            self.head = new_node

        # check if ll is not empty
            # we assign new node to the existing tail
        if self.tail:
            self.tail.next = new_node

        # add new node to tail
        self.tail = new_node

        # increase size by one
        self.size = self.size + 1

    def add_at_the_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def delete_at_begining(self):
        self.head = self.head.next
        self.size = self.size - 1

    def delete_at_the_end(self):
        # Node [data | next] -> Node [data | next] -> Node [data | next] -> Node [data | next]
        # previos
        # current
        #current = self.head
        #current.next = self. tail
        #self.tail = current
        current = self.head

        while current:
            # print('current',current)
            if current.next == self.tail:
                # print('current.next == self.tail',current.next == self.tail)
                self.tail = current
                self.tail.next = None
            current = current.next

    def delete_at_nth_node(self):
        pass


new_l = SinglyLinkedList()
new_l.add_at_the_end(10)
new_l.add_at_the_end(20)
new_l.add_at_the_end(30)
new_l.add_at_the_end(40)

# 10
# 20
# 30
# 40

# new_l.traverse()

new_l.delete_at_the_end()
new_l.traverse()
