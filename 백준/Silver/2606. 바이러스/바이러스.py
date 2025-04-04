from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    
    visited[start] = True
    
    while q:
        v = q.popleft()
        
        for i in graph[v]: 
            if not visited[i]:
                q.append(i)
                visited[i] = True

N = int(input())
V = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(V):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)  
bfs(1)  


cnt = -1 
for v in visited:
    if v:
        cnt += 1

print(cnt)