def dfs_rec(adj, visited, source):
    visited[source] = True
    print(source,end=" ")
    for i in adj[source]:
        if not visited[i]:
            dfs_rec(adj, visited, i)
            
def dfs(adj, source):
    visited = [False] * len(adj)
    dfs_rec(adj, visited, source)
    
def add_adj(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
    
v = 5
adj = [[] for _ in range(v)]
edges = [[0,1],[0,2],[1,3],[1,4],[2,4]]
for i in edges:
    add_adj(adj, i[0], i[1])
    
dfs(adj, 0)