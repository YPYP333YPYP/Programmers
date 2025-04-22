from collections import deque

dx = [0,-1,0,1,0,0]
dy = [-1,0,1,0,0,0]
dz = [0,0,0,0,-1,1]

def bfs(start, end, time, visited):
    q = deque()
    z,y,x = start
    q.append((z,y,x,time))
    visited[z][y][x] = True

    while q:
        z,y,x,t = q.popleft()
        for i in range(6):
            nx,ny,nz = x+dx[i], y+dy[i], z+dz[i]
            if (nz,ny,nx) == end:
                return t + 1
            if 0 <= nx < C and 0 <= ny < R  and 0<= nz < L and not visited[nz][ny][nx] and graph[nz][ny][nx] == '.':
                q.append((nz,ny, nx, t+1))
                visited[nz][ny][nx] = True
    return -1

while True:
    # 높이 -> L, 가로 길이 -> C, 세로 길이 -> R
    L, R, C = map(int, input().split())
    if L == 0:
        break
    graph = []
    start = set()
    end = set()
    for i in range(L):
        grid = []
        for j in range(R):
            tmp = []
            row = input()
            for k,v in enumerate(row):
                if v == 'S':
                    start = (i,j,k)
                if v == 'E':
                    end = (i,j,k)
                tmp.append(v)
            grid.append(tmp)
        graph.append(grid)
        _ = input()

    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    result = bfs(start, end, 0, visited)
    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")