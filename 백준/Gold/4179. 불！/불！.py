from collections import deque

R, C = map(int, input().split())

grid = [[] for _ in range(R)]
j_pos = None
f_pos = []

for i in range(R):
    row = input()  # split() 제거
    for j, v in enumerate(row):
        if v == 'J':
            j_pos = (i, j)
        if v == 'F':
            f_pos.append((i, j))
        grid[i].append(v)

visited_j = [[False] * C for _ in range(R)]
visited_f = [[False] * C for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(j, f):
    x, y = j
    q = deque()
    q.append((x, y, 0))
    fire_list = deque()

    for fx, fy in f:
        fire_list.append((fx, fy))
        visited_f[fx][fy] = True

    visited_j[x][y] = True

    while q:
        size = len(q)
        for _ in range(size):
            x, y, time = q.popleft()

            if grid[x][y] == 'F':
                continue

            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                return time + 1

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.' and not visited_j[nx][ny]:
                    q.append((nx, ny, time + 1))
                    visited_j[nx][ny] = True

        fire_size = len(fire_list)
        for _ in range(fire_size):
            fa, fb = fire_list.popleft()
            for i in range(4):
                nfa, nfb = fa + dx[i], fb + dy[i]
                if 0 <= nfa < R and 0 <= nfb < C:
                    if (grid[nfa][nfb] == '.' or grid[nfa][nfb] == 'J') and not visited_f[nfa][nfb]:
                        fire_list.append((nfa, nfb))
                        visited_f[nfa][nfb] = True
                        grid[nfa][nfb] = 'F'

    return -1


result = bfs(j_pos, f_pos)
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)