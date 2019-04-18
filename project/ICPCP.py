from Graph import Graph
from Vertex import Vertex


def main():
    D = input("How long to run the tasks?  ")

    G = Graph()

    """G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')
    G.add_vertex('f')

    G.add_edge('a', 'b', 7)
    G.add_edge('a', 'c', 9)
    G.add_edge('a', 'f', 14)
    G.add_edge('b', 'c', 10)
    G.add_edge('b', 'd', 15)
    G.add_edge('c', 'd', 11)
    G.add_edge('c', 'f', 2)
    G.add_edge('d', 'e', 6)
    G.add_edge('e', 'f', 9)"""

    schedule_workflow(G, D)



def calc_EST(node):
    pass

def calc_LFT(node):
    pass

def calc_EFT(node):
    pass

def calc_AST(node):
    pass

def schedule_workflow(G, D): #maybe T and E

    services = input("How many computers are available?  ")

    # Initialize Graph
    G.add_vertex('T_Entry')
    G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')
    G.add_vertex('f')
    G.add_vertex('T_Exit')

    #Initialize edges with weights
    G.add_edge('a', 'b', 7)
    G.add_edge('a', 'c', 9)
    G.add_edge('a', 'f', 14)
    G.add_edge('b', 'c', 10)
    G.add_edge('b', 'd', 15)
    G.add_edge('c', 'd', 11)
    G.add_edge('c', 'f', 2)
    G.add_edge('d', 'e', 6)
    G.add_edge('e', 'f', 9)

    #Calculate EST, AST, LFT, and EFT

    #AST(T_Entry) = 0, AST(T_Exit) = D

    #Set T_Entry and T_Exit as assigned
    G.get_vertex("T_Entry").set_assigned()
    G.get_vertex("T_Exit").set_assigned()

    #Call AssignParents for T_Exit
    assign_parents(G.get_vertex("T_Exit"))

def assign_parents(node):
    pass

"""
Algorithm 2 Parents Assigning Algorithm
1: procedure AssignParents(t)
2: while (t has an unassigned parent) do
3: PCP ← null, ti ← t
4: while (there exists an unassigned parent of ti) do
5: add CriticalParent(ti) to the beginning of PCP
6: ti ← CriticalParent(ti)
7: end while
8: call AssignPath(PCP)
9: for all (ti ∈ PCP) do
10: update EST and EFT for all successors of ti
11: update LFT for all predecessors of ti
12: call AssignParents(ti)
13: end for
14: end while
15: end procedure
"""


"""
Algorithm 3 Path Assigning Algorithm
1: procedure AssignPath(P)
2: si,j ← the cheapest applicable existing instance for P
3: if (si,j
is null) then
4: launch a new instance si,j of the cheapest service si which can finish each
task of P before its LFT
5: end if
6: schedule P on si,j and set SS(ti), AST (ti) for each ti ∈ P
7: set all tasks of P as assigned
8: end procedure
"""

"""
Algorithm 4 Planning Algorithm
1: procedure Planning(G(T , E))
2: Queue ← tentry
3: while (Queue is not empty) do
4: t ← delete first task from Queue
5: si,j ← the cheapest applicable existing instance for P
6: if (si,j
is null) then
7: launch a new instance si,j of the cheapest service si which can finish t
before its subdeadline
8: end if
9: schedule t on si,j and set SS(t) and AST (t)
10: for all (tc ∈ children of t) do
11: if (all parents of tc are scheduled) then
12: add tc to Queue
13: end if
14: end for
15: end while
16: end procedure
"""

"""MOVE calc_AST, calc_EFT, calc_EST, calc_LFT to graph creation process so it automatically calculates these values"""

main()
