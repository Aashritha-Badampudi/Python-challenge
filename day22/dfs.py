def dfs(adj,node,visited):
    if visited[node]==1:
        return
    visited[node]=1
    print(node)
    for i in adj[node]:
        dfs(adj,i,visited)

adj={
    1:[2],
    2:[1,3,4],
    3:[2,4],
    4:[2,3]
}
root=2
n=len(adj)
visited=[0 for i in range(n+1)]
dfs(adj,root,visited)
