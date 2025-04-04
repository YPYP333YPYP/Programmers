from collections import deque

N, M = map(int, input().split())

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    
    q = deque()
    q.append((x, y, 1))
    
    while q:
        x, y, dist = q.popleft()
        
        if x == N-1 and y == M-1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
    return -1

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

print(bfs(0,0))

    