from collections import deque

N = int(input())

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((x,y))
    
    visited[x][y] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny] :
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt +=1
    return cnt

total = 0
val = []
graph = []

for i in range(N):
    graph.append(list(map(int, input())))
    
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            total += 1
            val.append(bfs(i, j))
            
print(total)
val.sort()
for v in val:
    print(v)