from collections import deque

T = int(input())

for _ in range(T):
    w, h = map(int, input().split())

    graph = []
    fire = []
    pos = None

    for i in range(h):
        row = list(input())
        for j, v in enumerate(row):
            if v == '@':
                pos = (i, j)
            if v == '*':
                fire.append((i, j))
        graph.append(row)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]


    def bfs():
        q = deque()

        for fx, fy in fire:
            q.append((fx, fy, '*'))

        q.append((pos[0], pos[1], '@'))

        time = 0

        while q:
            if time == 0 and graph[pos[0]][pos[1]] == '@' and (
                    pos[0] == 0 or pos[0] == h - 1 or pos[1] == 0 or pos[1] == w - 1):
                return 1

            for _ in range(len(q)):
                x, y, type = q.popleft()

                if type == '@' and (x == 0 or x == h - 1 or y == 0 or y == w - 1) and time > 0:
                    return time + 1

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < h and 0 <= ny < w:
                        if type == '*' and graph[nx][ny] != '#' and graph[nx][ny] != '*':
                            graph[nx][ny] = '*'
                            q.append((nx, ny, '*'))
                        elif type == '@' and graph[nx][ny] == '.':
                            graph[nx][ny] = '@'
                            q.append((nx, ny, '@'))

            time += 1

        return "IMPOSSIBLE"


    print(bfs())