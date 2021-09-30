#-----------------------------------------------------------------------
# linkedstack.py
#-----------------------------------------------------------------------

from stdlib import stdio
import copy

# A Stack object is a last-in-first-out collection.

class Stack:

    #-------------------------------------------------------------------

    # Construct an empty Stack object.

    def __init__(self):
        self._first = None  # Reference to first _Node
        self._length = 0

    #-------------------------------------------------------------------

    # Return True if Stack object self is empty, and False otherwise.

    def isEmpty(self):
        return self._first is None

    #-------------------------------------------------------------------

    # Push item onto the top of 'self'.

    def push(self, item):
        self._first = _Node(item, self._first)
        self._length += 1

    #-------------------------------------------------------------------

    # Pop the top item from 'self' and return it.
    def pop(self):
        item = self._first.item
        self._first = self._first.next
        self._length -= 1
        return item
    
    def size(self):
        """
        Return the size of the stack.
        """
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

    # Return a string representation of 'self'.
    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s

#-----------------------------------------------------------------------

# A _Node object references an item and a next _Node object.
# A Stack object is composed of _Node objects.

class _Node:
    def __init__(self, item, next):
        self.item = item  # Reference to an item.
        self.next = next  # Reference to the next _Node object

#-----------------------------------------------------------------------

# For testing:

def main():
    stack = Stack()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            stack.push(item)
        else:
            stdio.write(stack.pop() + ' ')
    stdio.writeln()

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# more tobe.txt 
# to be or not to - be - - that - - - is

# python linkedstack.py < tobe.txt 
# to be not that or be 

