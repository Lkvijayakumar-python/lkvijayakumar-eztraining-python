# import dictionary for graph
from collections import defaultdict
# ADD EDGE TO GRAPH :FUNCTION
graph = defaultdict(list)
def addedge(graph,u,v):
    graph[u].append(v)

#FUNCTION DESCRIPTION
def generate_edges(graph):
    edges = []

    # for each node in graph
    for node in graph:
        # for each neighbour node of a single node
        for neighbour in graph[node]:

            #if edge exists then append
            edges.append((node,neighbour))
    return edges
#DECLARING -graph as dictionary
addedge(graph,'a','c')
addedge(graph,'b','c')
addedge(graph,'b','e')
addedge(graph,'c','c')
addedge(graph,'c','e')
addedge(graph,'c','a')
addedge(graph,'c','b')
addedge(graph,'e','b')
addedge(graph,'d','c')
addedge(graph,'e','c')

# PRINTING GRAPH
print(generate_edges(graph))
