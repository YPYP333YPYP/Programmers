from collections import deque

R, C = map(int, input().split())
graph = []

# 고슴도치, 비버 위치 초기화
hedgehog_pos = None
beaver_pos = None
water_positions = []

# 그래프 입력 받기
for i in range(R):
    row = list(input())
    graph.append(row)
    for j, cell in enumerate(row):
        if cell == 'S':
            hedgehog_pos = (i, j)
        elif cell == '*':
            water_positions.append((i, j))
        elif cell == 'D':
            beaver_pos = (i, j)

# 방향 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    # 방문 배열 초기화
    visited = [[False] * C for _ in range(R)]
    visited[hedgehog_pos[0]][hedgehog_pos[1]] = True

    # 큐 초기화 (위치, 시간, 타입)
    queue = deque()

    # 물 먼저 넣기
    for wx, wy in water_positions:
        queue.append((wx, wy, 0, 'water'))

    # 고슴도치 정보 넣기
    queue.append((hedgehog_pos[0], hedgehog_pos[1], 0, 'hedgehog'))

    while queue:
        x, y, time, type_id = queue.popleft()

        # 고슴도치가 비버의 굴에 도달한 경우
        if type_id == 'hedgehog' and graph[x][y] == 'D':
            return time

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 체크
            if not (0 <= nx < R and 0 <= ny < C):
                continue

            # 물인 경우
            if type_id == 'water':
                # 물은 빈 칸이나 고슴도치가 있는 칸으로만 확장 (비버의 굴로는 확장 불가)
                if graph[nx][ny] == '.' or graph[nx][ny] == 'S':
                    graph[nx][ny] = '*'
                    queue.append((nx, ny, time + 1, 'water'))

            # 고슴도치인 경우
            else:
                # 이미 방문했거나 물이나 돌이 있는 곳으로는 이동 불가
                if not visited[nx][ny] and graph[nx][ny] != '*' and graph[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1, 'hedgehog'))

    # 비버의 굴에 도달할 수 없는 경우
    return "KAKTUS"


print(bfs())