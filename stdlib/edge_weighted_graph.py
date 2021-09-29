#-----------------------------------------------------------------------
# edge_weighted_graph.py
#-----------------------------------------------------------------------

from stdlib import stdio
from stdlib.instream import InStream
from stdlib import Bag
from stdlib import Edge

#-----------------------------------------------------------------------
# The EdgeWeightedGraph class represents an edge-weighted
#  graph of vertices named 0 through V – 1, where each
#  undirected edge is of type Edge and has a real-valued weight.
#  It supports the following two primary operations: add an edge to the graph,
#  iterate over all of the edges incident to a vertex. It also provides
#  methods for returning the degree of a vertex, the number of vertices
#  Vin the graph, and the number of edges E in the graph.
#  Parallel edges and self-loops are permitted.
#-----------------------------------------------------------------------

class EdgeWeightedGraph:
    
    def __init__(self, V=0, filename=None):
        """
        Construct a new Graph object. If a filename is specified,
        populate the Graph object by reading data from the specified
        file.
        """

        self._e = 0   # number of edges
        
        self._adj = dict()

        if filename is not None:
            instream  = InStream(filename)

            # read the number of vertices
            self._v = instream.readInt()
            if self._v < 0:
                raise ValueError("number of edges in a Graph must be non-negative")
            
            for v in range(self._v):
                self._adj[v] = Bag()
            
            # read the number of edges
            e = instream.readInt()
            if e < 0:
                raise ValueError("number of edges in a Graph must be non-negative")
            
            for i in range(e):
                v = instream.readInt()
                w = instream.readInt()
                self._validVertex(v)
                self._validVertex(w)
                weight = instream.readFloat()
                e = Edge(v, w, weight)
                self.addEdge(e)
        else:
            self._v = V
            for v in range(self._v):
                self._adj[v] = Bag()
            
    def addEdge(self, edge: Edge):
        """
        Adds the undericted weighted edge to this graph
        """
        v = edge.either()
        w = edge.other(v)
        self._validVertex(v)
        self._validVertex(w)
        self._adj[v].add(edge)
        self._adj[w].add(edge)
        self._e += 1
    
    def hasEdge(self, v, w):
        pass
    
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
    
    def edges(self):
        """
        Returns all edges in this edge-weighted graph.
        """
        edgeList = Bag()

        for v in range(self._v):
            self_loops = 0
            for e in self._adj[v]:
                if e.other(v) > v:
                    edgeList.add(e)
                elif e.other(v) == v:
                    if self_loops % 2 == 0:
                        edgeList.add(e)
                    self_loops += 1
        
        return edgeList
    
    def __str__(self) -> str:
        """
        Returns a string representation of this graph.
        """
        s = "{0} vertercies, {1} edges\n".format(self.V(), self.E())

        for v in range(self.V()):
            s += str(v) + ": "
            for e in self.adj(v):
                s += str(e) + " "
            s += "\n"
        
        return s
        

    def  _validVertex(self, v):
        """
        raise a Value error unless 0 <= v < V
        """
        if v < 0 or v >= self._v:
            raise ValueError(f"vertex {v} is not between 0 and {self._v - 1}")



def main():
    graph = EdgeWeightedGraph("../data/tinyGW.txt")
    stdio.writeln(graph)
    print(graph.E())

if __name__ == '__main__':
    main()

