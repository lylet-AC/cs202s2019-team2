from Graph import Graph
from Vertex import Vertex

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print( vid, wid, v.get_weight(w))

    for v in g:
        print(v.get_id(), g.vert_dict[v.get_id()])

"""
G is the workfow Graph
T is a set of tasks
E is a set of dependencies (the order of execution)
D deadline that the tasks must be completed by

EST (earliest start time)
EFT (earliest finish time)
LFT (last finish time)
AST (actual start time) - complicated math that selects which task should run based on the jlfsajlfsdj;kldas

"""
