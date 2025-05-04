from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
wall = []  
graph = []
start = None

for i in range(N):
    row = input().split()
    for j, v in enumerate(row):
        if v == '2':
            start = (i, j)
        if v == '0':
            wall.append((i, j))
    graph.append(row)

visited = [[False] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]


def bfs(start):
    a, b = start
    q = deque([(a, b)])
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1


bfs(start)

wall_set = set(wall)
for i in range(N):
    for j in range(M):
        if (i, j) != start and graph[i][j] == '1' and distance[i][j] == 0:
            distance[i][j] = -1

# 결과 출력
for v in distance:
    print(*v)