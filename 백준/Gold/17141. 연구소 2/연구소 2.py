from collections import deque
import itertools

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

virus = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))

p_virus = list(itertools.combinations(virus, M))


def bfs(virus_list):
    q = deque()

    visited = [[0] * N for _ in range(N)]
    for x, y in virus_list:
        q.append((x, y))
        visited[x][y] = 1

    while q:
        x, y= q.popleft()

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and (graph[i][j] == 0 or graph[i][j] == 2):
                count += 1
    mx = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1:  # Skip walls
                mx = max(mx, visited[i][j])
    return mx - 1, count


result = float("Inf")

for v in p_virus:
    t, c = bfs(v)

    if t < result and c == 0:
        result = t

if result == float("Inf"):
    print(-1)
else:
    print(result)