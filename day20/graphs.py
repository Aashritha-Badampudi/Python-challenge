'''
Graphs:
------
1. Collection of nodes or data
2. Edge and vertices(vertex or node)
3. Vertices is a point or a node(Eg. source and destination in maps)
4. Edge is a connection between nodes or vertices(It is like a path from source to destination)
5. Graph is a combination of edges and vertices
6. G{V,E}

    (1)
   /   \
 (2)---(3)
  |     |
 (4)---(5)

 V = {1, 2, 3, 4, 5}
 E = {(1,2), (1,3), (2,3), (2,4), (3,5), (4,5)}

 Types of graphs:
 1. Directed : Will have directions i.e we will specify the path
 2. Undirected : Don't have any direction it is a bidirection
 3. Weighted : Edges will have the weights 
 4. Unweighted : No weights
 5. Connected : All the nodes/vertices are connected
 6. Disconnected/Unconnected/Non connected : vertices may or may not connected by edge
 7. Cyclic : Starting and ending from the same node
 8. Acyclic : There will be no cycles in the graph

 => There are 2 ways to implement:
 1. Adjacency list **G = [(1,2),(2,3),(3,4),(4,1),(2,4),(1,3)]**
 2. Adjacency matrix 

'''
g=[(1,2),(2,4),(4,9),(9,3),(3,1),(1,9)]
adj={}
for u,v in g:
    if u not in adj:
        adj[u]=[]
    if v not in adj:
        adj[v]=[]

    adj[u].append(v)
    adj[v].append(u)

print(adj)
      