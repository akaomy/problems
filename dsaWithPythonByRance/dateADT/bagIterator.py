class BagIterator:

    def __init__(self, _items):
        self._bagItems = _items
        self._currentItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._currentItem < len(self._bagItems):
            item = self._bagItems[self._currentItem]
            self._currentItem += 1
            return item
        else:
            raise StopIteration
