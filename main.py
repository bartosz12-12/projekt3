from queue import Queue
from enum import Enum
from typing import Any, Callable
from typing import Optional
from typing import Dict, List
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int):
        self.data = data
        self.index = index

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph():
    adjacencies: Dict[Vertex, List[Edge]]
    list_from = []
    list_to = []

    def __init__(self):
        self.adjacencies = {}
        self.list_from = []
        self.list_to = []

    def __str__(self):
        result = ""
        list1 = self.adjacencies.items()
        for key, value in list1:
            result += f'- {key.data}: {key.data} ----> [] \n'
        return result

    def create_vertex(self, data: Any):
        if not self.adjacencies:
            vertex = Vertex(data, 1)
            self.adjacencies[vertex] = []
        else:
            index = list(self.adjacencies.keys())[-1].index + 1
            vertex = Vertex(data, index)
            self.adjacencies[vertex] = []
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)
        self.list_from.append(source.data)
        self.list_to.append(destination.data)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        edge1 = Edge(source, destination, weight)
        edge2 = Edge(destination, source, weight)

        self.adjacencies[source].append(edge1)
        self.adjacencies[destination].append(edge2)

        self.list_from.append(source.data)
        self.list_from.append(destination.data)
        self.list_to.append(destination.data)
        self.list_to.append(source.data)


    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        if edge == EdgeType.undirected:
            self.add_undirected_edge(source, destination, weight)


    def show(self):
        relacja = pd.DataFrame({'from': [x for x in self.list_from],
                                      'to': [y for y in self.list_to]})
        # print(relacja)
        g = nx.from_pandas_edgelist(relacja, 'from', 'to', create_using=nx.DiGraph())
        nx.draw(g, with_labels=True, arrows=True)
        plt.show()


    def dfs(self,v: Vertex, visited: List[Vertex], visit: Callable[[Any], None],stop:Vertex):
        visit(v)
        visited.append(v)
        if stop in visited:
            return
        for neighbour in self.adjacencies[v]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination, visited, visit,stop)
            if stop in visited:
                return

    def traverse_depth_first(self,v,visit: Callable[[Any], None],stop):
        vertices = list(self.adjacencies.keys())
        visited = []
        self.dfs(vertices[v], visited, visit, vertices[stop])


    def all_weighted_shortest_paths(self,start:Any,stop):
        self.traverse_depth_first(start, visit, stop)




def visit(vertex: Any) -> None:
    print(vertex.data)

graf1 = Graph()

graf1.create_vertex("v0")
graf1.create_vertex("v1")
graf1.create_vertex("v2")
graf1.create_vertex("v3")
graf1.create_vertex("v4")
graf1.create_vertex("v5")

vertex = list(graf1.adjacencies.keys())
y = len(vertex)
graf1.add_undirected_edge(vertex[0], vertex[1], None)
graf1.add_undirected_edge(vertex[1], vertex[5], None)
graf1.add_undirected_edge(vertex[0], vertex[5], None)
graf1.add_undirected_edge(vertex[0], vertex[4], None)
graf1.add_undirected_edge(vertex[4], vertex[5], None)
graf1.add_undirected_edge(vertex[2], vertex[1], None)
graf1.add_undirected_edge(vertex[1], vertex[2], None)
graf1.add_undirected_edge(vertex[1], vertex[3], None)

# graf1.show()
# lista = list(range(y))
# for x in lista:
#     graf1.all_weighted_shortest_paths(0, x)
#     print("\n")
##############################################################


graf2 = Graph()

graf2.create_vertex("v0")
graf2.create_vertex("v1")
graf2.create_vertex("v2")
graf2.create_vertex("v3")
graf2.create_vertex("v4")
graf2.create_vertex("v5")

vertex2 = list(graf2.adjacencies.keys())

graf2.add_directed_edge(vertex2[0], vertex2[5], None)
graf2.add_directed_edge(vertex2[5], vertex2[1], None)
graf2.add_directed_edge(vertex2[1], vertex2[0], None)
graf2.add_directed_edge(vertex2[1], vertex2[3], None)
graf2.add_directed_edge(vertex2[1], vertex2[2], None)
graf2.add_directed_edge(vertex2[2], vertex2[4], None)
graf2.add_directed_edge(vertex2[4], vertex2[0], None)

y2 = len(vertex2)
graf2.show()
lista2 = list(range(y2))
for x2 in lista2:
    graf2.all_weighted_shortest_paths(0, x2)
    print("\n")

#########################################################

graf3 = Graph()

graf3.create_vertex("v0")
graf3.create_vertex("v1")
graf3.create_vertex("v2")

vertex3 = list(graf3.adjacencies.keys())

graf3.add_undirected_edge(vertex3[0], vertex3[1], None)
graf3.add_undirected_edge(vertex3[1], vertex3[2], None)
graf3.add_undirected_edge(vertex3[2], vertex3[0], None)

# y3 = len(vertex3)
# graf3.show()
# lista3 = list(range(y3))
# for x3 in lista3:
#     graf3.all_weighted_shortest_paths(1, x3)
#     print("\n")
