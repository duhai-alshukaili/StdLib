#-----------------------------------------------------------------------
# linkedqueue.py
#-----------------------------------------------------------------------

from stdlib import stdio
import copy

# A Queue object is a first-in-first-out container.

class Queue:

    #-------------------------------------------------------------------

    # Construct Queue object self as an empty Queue object.

    def __init__(self):
        self._first = None  # Reference to first _Node
        self._last = None   # Reference to last _Node
        self._length = 0    # Number of items

    #-------------------------------------------------------------------

    # Return True if self is empty, and False otherwise.

    def isEmpty(self):
        return self._first is None

    #-------------------------------------------------------------------

    # Add item to the end of self.
    def enqueue(self, item):
        oldLast = self._last
        self._last = _Node(item, None)
        if self.isEmpty():
            self._first = self._last
        else:
            oldLast.next = self._last
        self._length += 1

    #-------------------------------------------------------------------

    # Remove the first item of self and return it.
    def dequeue(self):
        item = self._first.item
        self._first = self._first.next
        if self.isEmpty():
            self._last = None
        self._length -= 1
        return item
    
    def size(self):
        return self._length

    #-------------------------------------------------------------------

    def __len__(self):
        """
        Return the number of items in self
        """
        return self._length

    def __iter__(self):
        """
        Return an iterator
        """
        self.__current = self._first
        return self
    
    def __next__(self):
        """
        Get the next item in the iteration
        """
        if self.__current is not None:
            item = copy.deepcopy(self.__current.item)
            self.__current = self.__current.next
            return item
        else:
            raise StopIteration

    #-------------------------------------------------------------------

    def __str__(self):
        """
        Return a string representation of the stack
        """
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s

#----------------------------------------------------------------------

# A _Node object references an item and a next _Node object.
# A Queue object is composed of _Node objects.

class _Node:
    def __init__(self, item, next):
        self.item = item  # Reference to an item
        self.next = next  # Reference to the next _Node object

#-----------------------------------------------------------------------

# Test the Queue class by reading strings from standard input and
# enqueueing or dequeueing as indicated. A minus sign indicates dequeue
# (and write to standard output), and any other string indicates
# enqueue.

def main():
    queue = Queue()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            queue.enqueue(item)
        else:
            stdio.write(queue.dequeue())
            stdio.write(' ')
    stdio.writeln()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# more tobe.txt
# to be or not to - be - - that - - - is

# python linkedqueue.py < tobe.txt
# to be or not to be

