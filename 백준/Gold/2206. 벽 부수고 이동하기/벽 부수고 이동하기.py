from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N):
    row = input()
    for j, v in enumerate(row):
        graph[i].append(v)

# 3차원 visited 배열: [x좌표][y좌표][벽을 부순 상태]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    q = deque()
    # (x, y, 이동 횟수, 벽을 부순 상태)
    q.append((0, 0, 1, 0))
    visited[0][0][0] = True

    while q:
        x, y, t, wall_broken = q.popleft()

        if x == N - 1 and y == M - 1:
            return t

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 빈 공간인 경우
                if graph[nx][ny] == '0' and not visited[nx][ny][wall_broken]:
                    visited[nx][ny][wall_broken] = True
                    q.append((nx, ny, t + 1, wall_broken))

                # 벽인 경우, 아직 벽을 부수지 않았다면 부술 수 있음
                elif graph[nx][ny] == '1' and wall_broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, t + 1, 1))

    return -1


result = bfs()
print(result)