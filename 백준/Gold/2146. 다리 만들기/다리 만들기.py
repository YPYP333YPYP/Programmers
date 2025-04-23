from collections import deque
import math

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 1

def bfs(x, y):
    global cnt
    q = deque()
    visited[x][y] = True
    graph[x][y] = cnt  # 섬에 번호 부여 추가
    q.append((x, y))

    result = []
    result.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                graph[nx][ny] = cnt  # 방문한 섬에 번호 부여
                result.append((nx, ny))

    cnt += 1
    return result

land = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            land.append(bfs(i, j))

def bfs_2(x, y, v):
    color = graph[x][y]  # 현재 섬의 번호
    q = deque()
    q.append((x, y, 0))  # (좌표x, 좌표y, 거리)
    v[x][y] = True

    while q:
        x, y, t = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny]:
                # 다른 섬에 도달한 경우
                if graph[nx][ny] != 0 and graph[nx][ny] != color:
                    return t
                # 바다인 경우 계속 탐색
                elif graph[nx][ny] == 0:
                    v[nx][ny] = True
                    q.append((nx, ny, t+1))

    return math.inf  # 도달할 수 없는 경우 무한대 반환

result = math.inf
# 섬의 가장자리인지 확인하는 함수 추가
def is_edge(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            return True
    return False
for pos in land:
    for p in pos:
        i, j = p
        if is_edge(i, j):  # 가장자리 셀만 확인 (최적화)
            v = [[False] * N for _ in range(N)]
            result = min(bfs_2(i, j, v), result)



print(result)