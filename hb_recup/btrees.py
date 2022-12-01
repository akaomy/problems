from select import select
from turtle import left, right


class Node:

    def __init__(self, data):
        self.left = left
        self.right = right
        self.data = data

    def insert(self, value):
        # if entered value is less then in the current node data
        if value <= self.data:
            # if there are no left nodes
            if left == None:
                # assign new node with given value to the left side
                left = Node(value)
        # if entered value is more than in the current node data
        else:
            # and if there are no right nodes
            if right == None:
                # assign new node with given value to the right side
                right = Node(value)
            else:
                # if there are right nodes insert value into it
                right.insert(value)

    # def if_contains():
        # if
