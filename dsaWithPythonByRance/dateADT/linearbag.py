
import bagIterator

# list based implementation

class Bag:

    # creates empty list
    def __init__(self):
        self._items = list()

    # returns # of items in the bag
    def __len__(self):
        return len(self._items)

    # checks if specific items is in the list
    def __contains__(self, item):
        return item in self._items

    # adds items to the list
    def add(self, item):
        self._items.append(item)
    
    # removes and returns an instance of the given item in the bag
    def remove(self, item):
        assert self._items in self._items, "The item must be in the bag"
        ndx = self._items.index(item)
        return self._items.pop(ndx)
    
    # returns an iterator for traversing the list of items
    def __iter__(self, item):
        return bagIterator.BagIterator(self._items)

# empty bag -> empty list
# bag size -> list size
# check for specific item -> use built in operation
# add item -> append it at the end of the list since it doesn't specify addition order
# removing item -> use built in operation
# iterate items -> use fo rloop