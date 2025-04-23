from collections import deque

K = int(input())
W, H = map(int, input().split())

graph = []

for _ in range(H):
    row = list(map(int, input().split()))
    graph.append(row)

# 원숭이 이동 방향 (상하좌우)
monkey_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 말 이동 방향 (8방향)
horse_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]


def bfs():
    # 큐: (y좌표, x좌표, 이동 횟수, 남은 말 이동 횟수)
    q = deque([(0, 0, 0, K)])
    visited[0][0][K] = True

    while q:
        y, x, count, horse_remain = q.popleft()

        # 목적지에 도착한 경우
        if y == H - 1 and x == W - 1:
            return count

        # 1. 원숭이처럼 이동 (상하좌우)
        for dy, dx in monkey_moves:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx][horse_remain] and graph[ny][nx] == 0:
                visited[ny][nx][horse_remain] = True
                q.append((ny, nx, count + 1, horse_remain))

        # 2. 말처럼 이동 (아직 횟수가 남아있을 경우)
        if horse_remain > 0:
            for dy, dx in horse_moves:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx][horse_remain - 1] and graph[ny][nx] == 0:
                    visited[ny][nx][horse_remain - 1] = True
                    q.append((ny, nx, count + 1, horse_remain - 1))

    # 목적지에 도달할 수 없는 경우
    return -1


print(bfs())