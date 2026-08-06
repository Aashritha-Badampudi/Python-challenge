'''
BFS-Breadth First Search:
It is used to print the data in the output
'''
adj={
    1:[2,4],
    2:[1,3,5],
    3:[2,5,4],
    4:[1,3],
    5:[2,3]
}
root=2
n=len(adj)
visited=[]
for i in range(n+1):
    visited.append(0)
a=[root]
op=[]
while len(a)!=0:
    k=a.pop(0)
    op.append(k)
    visited[k]=1
    for j in adj[k]:
        if visited[j]==0:
            visited[j]=1
            a.append(j)

print(op)