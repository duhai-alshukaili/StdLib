#-----------------------------------------------------------------------
# minpqueue.py
#-----------------------------------------------------------------------

from stdlib import stdio
import copy

# The MinPQ object represents a priority queue of generic keys.
# It supports the usual <em>insert</em> and <em>delete-the-minimum</em>
# operations, along with methods for peeking at the minimum key,
# testing if the priority queue is empty, and iterating through
# the keys.

class MinPQ:

    def __init__(self, init_capacity=1):
        self._pq = [None] * (init_capacity + 1)
        self._n  = 0
    
    # def __init__(self, keys=None):
    #     """
    #     Initializes a priority queue from the array of keys.

    #     Arguments:
    #     keys -- an array of keys to be added to the queue.
    #     """
    #     if not hasattr(keys, '__iter__'):
    #         raise AttributeError("keys argument must be an iterable.")
        
    #     self._n = len(keys)
    #     self._pq = [None] * (len(keys) + 1)

    #     for i in range(self._n):
    #         self._pq[i+1] = keys[i]
        
    #     for k in range(self._n // 2, 0, -1):
    #         self._sink(k)
        
    #     assert self._isMinHeap()

    def isEmpty(self):
        """
        Returns True if this priority queue is empty.
        """
        return self._n == 0

    def size(self):
        """
        Returns the number of keys on this priority queue.
        """
        return self._n

    def min(self):
        """
        Returns a smallest key on this priority queue.
        """
        if self.isEmpty():
            raise  IndexError("Priority queue underflow")
        return self._pq[1]
        
    def insert(self, key):
        """
        Adds a new key to this priority queue.
        """
        # double size of array if necessary
        if self._n == len(self._pq) - 1:
            self._resize(2 * len(self._pq))
        
        # add key, and percolate it up to maintain heap invariant
        self._n += 1
        self._pq[self._n] = key
        self._swim(self._n)
        assert self._isMinHeap()
    
    def delMin(self):
        """
        Removes and returns a smallest key on this priority queue.
        """
        if self.isEmpty():
            raise  IndexError("Priority queue underflow")
        
        min = self._pq[1]

        self._exch(1, self._n) # exchange the first item with the last item
        self._n -= 1  # reduce the length by 1
        self._sink(1) # sink the item in the top 
        self._pq[self._n + 1] = None # help with garbage collection

        if self._n > 0 and (self._n == (len(self._pq) - 1) // 4): # if list is 1/4 full
            self._resize(len(self._pq) // 2)  # resize to 1/2 the current size
        
        assert self._isMinHeap()

        return min
    
    def __len__(self):
        return self._n
    
    def __iter__(self):
        # create a copy pq
        self.__copy = MinPQ()  # initialize the iterator by creating a copy
        for i in range(1, self._n + 1):
            self.__copy.insert(copy.deepcopy(self._pq[i]))

        return self
    
    def __next__(self):
        if not self.__copy.isEmpty():
            return self.__copy.delMin()
        else:
            raise StopIteration

    # --------------------------------------------------
    # Helper functions to restore the heap invariant.
    # --------------------------------------------------
    def _resize(self, capacity):
        """
        Resize the underlying array to have the given capacity
        """
        assert capacity > self._n
        temp = [None] * capacity
        for i in range(1, self._n + 1):
            temp[i] = self._pq[i]
        self._pq = temp

    def _swim(self, k):
        while k > 1 and self._greater(k//2, k):
            self._exch(k, k//2)
            k = k//2
    
    def _sink(self, k):
        while 2 * k <= self._n:
            j = 2 * k
            if j < self._n and self._greater(j, j + 1):
                j += 1
            if not self._greater(k, j):
                break
            self._exch(k, j)
            k = j

    # --------------------------------------------------
    # Helper functions for compares and swaps.
    # --------------------------------------------------
    def _greater(self, i, j):
        return self._pq[i] > self._pq[j]
    
    def _exch(self, i, j):
        temp = self._pq[i]
        self._pq[i] = self._pq[j]
        self._pq[j] = temp
    
    def _isMinHeap(self):
        """
        Is pq[1..n] a min heap?
        """
        for i in range(1, self._n+1):
            if self._pq[i] is None:
                return False

        for i in range(self._n + 1, len(self._pq)):
            if self._pq[i] is not None:
                return False
        
        if self._pq[0] is not None:
            return False
        
        return self._isMinHeapOrdered(1)

    def _isMinHeapOrdered(self, k):
        """
        Is subtree of pq[1..n] rooted at k a min heap?
        """
        if k > self._n:
            return True
        
        left = 2 * k
        right = 2 * k + 1
        
        if left <= self._n and self._greater(k, left):
            return False
        
        if right <= self._n and self._greater(k, right):
            return False
        
        return self._isMinHeapOrdered(left) and self._isMinHeapOrdered(right)
        
# Test the MinPQ class by reading strings from standard input and
# inserting or deleting them as indicated. A minus sign indicates deleting 
# the minimum key (and write to standard output), and any other string 
# indicate and insert.

def main():
    queue = MinPQ()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            queue.insert(item)
            # stdio.writeln("{} items in the queue".format(queue.size()))
        else:
            if not queue.isEmpty():
                stdio.write(queue.delMin())
                stdio.write(" ")
    stdio.writeln()

if __name__ == '__main__':
    main()
    
