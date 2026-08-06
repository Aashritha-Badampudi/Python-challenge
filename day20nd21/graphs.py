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
 2. Adjacency matrix :
                       1 2 3 4 5
                   1 [ 0 1 1 0 0 ]
                   2 [ 1 0 1 1 0 ]
                   3 [ 1 1 0 0 1 ]
                   4 [ 0 1 0 0 1 ]
                   5 [ 0 0 1 1 0 ]

'''
#Creating Adjacency list
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

#Sir method for creating adjacency list:
g=[(1,2),(2,4),(4,9),(9,3),(3,1),(1,9)]
adj={}
for i in g:
    if i[0] not in adj:
        adj[i[0]]=[]
    adj[i[0]].append(i[1])
    if i[1] not in adj:
        adj[i[1]]=[]
    adj[i[1]].append(i[0])

print(adj)

'''
Graph and matrix for weighted graph
g=[(v,v,w)]
Eg: g=[(0,1,3),(1,2,9),(2,3,5),(3,0,6),(0,2,11),(1,3,2)]
        3
   (0)------(1)
    |\      /|
    | \11  / |
   6|  \  / 2|9
    |   \/   |
    |   /\   |
   (3)------(2)
        5

    0  1  2  3
0 [ 0, 3,11, 6 ]
1 [ 3, 0, 9, 2 ]
2 [11, 9, 0, 5 ]
3 [ 6, 2, 5, 0 ]
       
'''      
#Code for adjacency matrix
