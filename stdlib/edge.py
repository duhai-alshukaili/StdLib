# -----------------------------------------------------------------------
# edge.py
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------
# The Edge class represent a weighted edged in an
# EdgeWeightedGraph. Each edge consists of two integers
# (naming the two vertices) and a real-value weight. he data type
# provides methods for accessing the two endpoints of the edge and
# the weight. The natural order for this data type is by
# ascending order of weight.
# -----------------------------------------------------------------------

class Edge:

    def __init__(self, v, w, weight):
        if v < 0:
            raise ValueError("vertex index must be a non-negative integer")
        if w < 0:
            raise ValueError("vertex index must be a non-negative integer")
        
        self._v = v
        self._w = w
        self._weight = weight
    
    @property
    def weight(self):
        """
        Returns the weight of this edge.
        """
        return self._weight
    
    
    def either(self):
        """
        Returns either endpoint of this edge.
        """
        return self._v
    
    def other(self, vertex):
        """
        Returns the endpoint of this edge that is different from the given vertex.
        """
        if vertex == self._v:
            return self._w
        
        elif vertex == self._w:
            return self._v
        
        else:
            raise ValueError("Illegal endpoint")
    
    def __str__(self) -> str:
        """
        Returns a string representation of this edge.
        """
        return f"{self._v:d}-{self._w:d} {self._weight:.5f}"
    

    def __repr__(self) -> str:
        """
        Returns a string representation of this edge.
        """
        return f"{self._v:d}-{self._w:d} {self._weight:.5f}"
    
    # methods to provide total ordering based on the weight
    def __eq__(self, other):
        return self.weight == other.weight
    
    def __ne__(self, other):
        return self.weight != other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __le__(self, other):
        return self.weight <= other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def __ge__(self, other):
        return self.weight >= other.weight
        
    