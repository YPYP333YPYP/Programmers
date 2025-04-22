from collections import deque
T = int(input())


def bfs(x, y, ex, ey, time, visited):
    q = deque()
    q.append((x,y, time))
    visited[x][y] = True

    while q:
        x,y,t = q.popleft()
        for dx,dy in [(-2,-1), (-1,-2), (-2,1), (-1,2), (1,-2), (2,-1), (2,1), (1,2)]:
            nx,ny = x+dx, y+dy
            if (nx,ny) == (ex,ey):
                return t + 1
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append((nx,ny, t+1))
                visited[nx][ny] = True

for _ in range(T):
    N = int(input())
    grid = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    a,b = map(int, input().split())
    start = (a,b)
    c,d = map(int, input().split())
    end = (c,d)
    if (a,b) == (c,d):
        print(0)
    else:
        result = bfs(start[0], start[1], end[0], end[1], 0, visited)
        print(result)