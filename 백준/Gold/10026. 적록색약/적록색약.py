from collections import deque

N = int(input())

grid_c1 = [[]* N for _ in range(N)]
grid_c2 = [[]* N for _ in range(N)]

for i in range(N):
    row = list(map(str, input().split()))
    for r in row:
        for v in r:
            grid_c1[i].append(v)
            if v == 'G':
                grid_c2[i].append('R')
            else:
                grid_c2[i].append(v)

visited_c1 = [[False] * N for _ in range(N)]
visited_c2 = [[False] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x,y,color,grid, visited):
    q = deque()
    q.append((x,y,color))
    visited[x][y] = True

    while q:
        x,y,c = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == c and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny, grid[nx][ny]))

    return 1

cnt_c1 = 0
cnt_c2 = 0

for i in range(N):
    for j in range(N):
        if not visited_c1[i][j]:
            cnt_c1 += bfs(i,j,grid_c1[i][j], grid_c1, visited_c1)
        if not visited_c2[i][j]:
            cnt_c2 += bfs(i,j,grid_c2[i][j], grid_c2, visited_c2)

print(f'{cnt_c1} {cnt_c2}')
