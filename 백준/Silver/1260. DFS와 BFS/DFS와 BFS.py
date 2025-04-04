from collections import deque

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            
def bfs(start):
    visited[start] = True
    queue = deque([start])

    while queue:
        q = queue.popleft()
        print(q, end=' ')

        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(1, n+1):
    graph[i].sort()
    
visited = [False] * (n+1)
dfs(v)

print()

visited = [False] * (n+1)
bfs(v)
    