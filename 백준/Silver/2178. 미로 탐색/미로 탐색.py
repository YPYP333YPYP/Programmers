from collections import deque

N, M = map(int, input().split())

tmp = [list(map(str, input().split())) for _ in range(N)]
graph = [[] * M for _ in range(N)]
for i in range(N):
    for v in tmp[i]:
        for j in v:
            graph[i].append(int(j))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * M for _ in range(N)]
dist = [[0]*M for _ in range(N)]

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True
    dist[sx][sy] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1


bfs(0,0)
print(dist[N-1][M-1])