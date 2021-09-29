from stdlib import EdgeWeightedGraph
from stdlib import stdio


def main():
    graph = EdgeWeightedGraph(filename="data/tinyGW.txt")
    stdio.writeln(graph)
    print(graph.E())

if __name__ == '__main__':
    main()