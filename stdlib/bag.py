# -----------------------------------------------------------------------
# bag.py
# -----------------------------------------------------------------------

from stdlib import stdio

# -----------------------------------------------------------------------
# The Bag class represents a bag (or multiset) of
# generic items. It supports insertion and iterating over the
# items in arbitrary order. This implementation uses a singly
# linked list with a nested class _Node.

# A generic bag or multiset, implemented using a singly linked list.

# % more tobe.txt
# to be or not to - be - - that - - - is

# % python bag.py < tobe.txt
# size of bag = 14
# is
# -
# -
# -
# that
# -
# -
# be
# -
# to
# not
# or
# be
# to
# -----------------------------------------------------------------------


class Bag:

    # Inner Node class
    class _Node:
        def __init__(self, item=None):
            self._item = item
            self._next = None

        @property
        def item(self):
            return self._item

        @item.setter
        def item(self, value):
            self._item = value

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, value):
            self._next = value

    def __init__(self):
        """
        Initializes an empty bag.
        """
        self._first = None
        self._n = 0

    def isEmpty(self):
        """
        Returns true if this bag is empty.
        """
        return self._first is None

    def size(self):
        """
        Returns the number of items in this bag.
        """
        return self._n

    def add(self, item):
        """
        Adds the item to this bag.
        """
        oldfirst = self._first
        self._first = self._Node()
        self._first.item = item
        self._first.next = oldfirst
        self._n += 1

    def __len__(self):
        return self._n

    def __iter__(self):
        self.__current = self._first
        return self

    def __next__(self):
        if self.__current is not None:
            item = self.__current.item
            self.__current = self.__current.next
            return item
        else:
            raise StopIteration


def main():
    bag = Bag()
    while not stdio.isEmpty():
        item = stdio.readString()
        bag.add(item)

    stdio.writeln("Size of the bag = {}".format(bag.size()))

    for item in bag:
        print(item)


if __name__ == '__main__':
    main()
