from collections import deque

M, N, K = map(int, input().split())

paper = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1 ,0 ,1]

visited = [[False]*N for _ in range(M)]
def bfs(x,y):
    cnt = 0
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and paper[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1

    return cnt + 1


result = []
total = 0

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0 and not visited[i][j]:
            result.append(bfs(i,j))
            total += 1

result.sort()

print(total)
print(*result, sep=' ')