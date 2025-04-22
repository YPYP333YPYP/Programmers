from collections import deque
T = int(input())

def bfs(x,y, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = True
    return 1

for i in range(T):
    M, N, K = map(int, input().split())
    grid = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        grid[b][a] = 1
    visited = [[False]*M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and not visited[i][j]:
                result += bfs(i,j,visited)
    print(result)