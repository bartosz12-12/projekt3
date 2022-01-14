from enum import Enum
from typing import Any
from typing import Optional
from typing import Dict, List

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data:Any
    index:int
    def __init__(self, data: Any, index:int):
        self.data = data
        self.index = index

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
    def __init__(self, source: Vertex,destination: Vertex,weight:Optional[float]):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph():
    adjacencies: Dict[Vertex, List[Edge]]
    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self,data:Any):
        if not self.adjacencies:
            vertex = Vertex(data,1)
            self.adjacencies[vertex]=[]
        else:
            index = list(self.adjacencies.keys())[-1].index+1
            vertex = Vertex(data,index)
            self.adjacencies[vertex]=[]
        return vertex
    def add_directed_edge(self,source:Vertex,destination:Vertex,weight:Optional[float]=None):
        edge = Edge(source,destination,weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self,source:Vertex,destination:Vertex,weight:Optional[float]=None):
        edge1 = Edge(source,destination,weight)
        edge2 = Edge(destination,source,weight)

        self.adjacencies[source].append(edge1)
        self.adjacencies[destination].append(edge2)

    def add(self,edge:EdgeType,source:Vertex,destination:Vertex,weight:Optional[float]=None):
        if edge==EdgeType.directed:
            self.add_directed_edge(source,destination,weight)
        if edge==EdgeType.undirected:
            self.add_undirected_edge(source,destination,weight)











