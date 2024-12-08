from collections import deque

def bfs(adj, source):
    visited = [False] * len(adj)
    visited[source] = True
    q = deque()
    q.append(source)
    while q:
        curr = q.popleft()
        print(curr,end=" ")
        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

def add_adj(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
    

v = 5
edges = [[0,1],[0,2],[1,3],[1,4],[2,4]]
adj = [[] for _ in range(v)]

for i in edges:
    add_adj(adj, i[0], i[1])
    
bfs(adj, 0)
