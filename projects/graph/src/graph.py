"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # initialize an empty object for the vertices
        self.vertices = {}
        # each vertices[index] Vertex() will have an associated object of edges found in vertices[index].edges

        # method to add a vertex to the vertices object
    def add_vertex(self, vertex_value):
        self.vertices[vertex_value] = Vertex(vertex_value)
        # constructs a new Vertex with the class constructor below

        # method to add edges to an existing vertex
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
            # connect the two vertices by giving each their respective edge
        else:
            raise IndexError('Vertex not found.')
            # return an error if either vertex does not exist

class Vertex:
    def __init__(self, vertex_value):
        self.value = vertex_value
        self.edges = set()

    # define the printable representation of the Vertex's edges object to be human-readable in the console
    # this prevents the '__main__.Object at 0x1234f' gobbledygook from logging in the console
    def __repr__(self):
        return f'{self.edges}'

# test the Graph class
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)