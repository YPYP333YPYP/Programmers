from collections import deque
n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y, visited):
    q = deque()
    q.append((x,y))
    
    union = []
    union.append((x,y))
    visited[x][y] = True
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            
            if 0 <= na < n and 0<= nb < n and not visited[na][nb]:
                if l<= abs(graph[a][b] - graph[na][nb]) <= r:
                    visited[na][nb] = True
                    q.append((na,nb))
                    union.append((na,nb))
    if len(union) <= 1:
        return 0
    sm = sum(graph[c][d] for c,d in union) // len(union)
    for c,d in union:
        graph[c][d] = sm
    return 1
day = 0
while True:
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(i,j,visited)
    if cnt == 0:
        break
    day += 1
print(day)