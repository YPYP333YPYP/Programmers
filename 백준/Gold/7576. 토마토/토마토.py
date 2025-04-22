from collections import deque

R, C = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(C)]

tomato = []
for i in range(C):
    for j in range(R):
        if graph[i][j] == 1:
            tomato.append((i, j))

visited = [[False] * R for _ in range(C)]

def bfs(tomato_list):
    time = 0
    q = deque(tomato_list)
    for x, y in tomato_list:
        visited[x][y] = True

    while q:
        size = len(q)
        if size == 0:
            break
        for _ in range(size):
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < C and 0 <= ny < R and not visited[nx][ny] and graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = 1
        time += 1
    return time - 1

def check(grid):
    for i in range(C):
        for j in range(R):
            if grid[i][j] == 0:
                return False
    return True


result = bfs(tomato)

if check(graph):
    print(result)
else:
    print(-1)