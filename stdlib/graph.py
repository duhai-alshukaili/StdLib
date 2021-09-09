#-----------------------------------------------------------------------
# graph.py
#-----------------------------------------------------------------------

from stdlib import stdio
from stdlib.instream import InStream

class Graph:

    def __init__(self, filename=None):
        """
        Construct a new Graph object. If a filename is specified,
        populate the Graph object by reading data from the specified
        file.
        """
        self._e = 0   # number of edges
        self._v = 0   # number of vertices
        self._adj = dict()

        if filename is not None:
            instream = InStream(filename)

            # read the number of vertices
            self._v = instream.readInt()
            if self._v < 0:
                raise ValueError("number of edges in a Graph must be non-negative") 
            
            for v in range(self._v):
                self._adj[v] = list()

            # read the number of edges
            e = instream.readInt()
            if e < 0:
                raise ValueError("number of edges in a Graph must be non-negative") 
            
            for i in range(e):
                v = instream.readInt()
                w = instream.readInt()
                self._validVertex(v)
                self._validVertex(w)
                self.addEdge(v, w)

        
    def  _validVertex(self, v):
        """
        raise a Value error unless 0 <= v < V
        """
        if v < 0 or v >= self._v:
            raise ValueError(f"vertex {v} is not between 0 and {self._v - 1}")
    
    def addEdge(self, v, w):
        """
        Adds the undirected edge v-w to this graph.
        """
        self._validVertex(v)
        self._validVertex(w)
        if not self.hasEdge(v, w):
            self._e += 1

            if w not in  self._adj[v]:
                self._adj[v].append(w)
            
            if v not in  self._adj[w]:
                self._adj[w].append(v)

    
    def hasEdge(self, v, w):
        """
        Return True if v-w is an edge in self, and False otherwise.
        """
        return w in self._adj[v]
    
    def adj(self, v):
        """
        Returns the vertices adjacent to vertex v
        """
        self._validVertex(v)
        return iter(self._adj[v])
    

    def degree(self, v):
        """
        Returns the degree of the vertex v
        """
        self._validVertex(v)
        return len(self._adj[v])
    

    def V(self):
        """
        Returns the number of vertices in this graph
        """
        return len(self._adj)
    
    def E(self):
        """
        Retuns the number of edges in this graph
        """
        return self._e
    
    def __str__(self) -> str:
        """
        Returns a string representation of this graph.
        """
        s = "{0} vertercies, {1} edges\n".format(self.V(), self.E())

        for v in range(self.V()):
            s += str(v) + ": "
            for w in self.adj(v):
                s += str(w) + " "
            s += "\n"
        
        return s

    

def main():
    graph = Graph("tinyG.txt")
    stdio.writeln(graph)
    print(graph.E())

if __name__ == '__main__':
    main()



