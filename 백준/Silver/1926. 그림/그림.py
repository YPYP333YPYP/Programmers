from collections import deque

# n -> 세로 길이, m -> 가로 길이
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True
    cnt = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1

    return cnt

extent = 0
total = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            total += 1
            value = bfs(i,j)
            extent = max(extent, value)

print(total)
print(extent)