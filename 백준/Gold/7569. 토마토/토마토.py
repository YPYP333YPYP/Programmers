from collections import deque

m, n, h = map(int, input().split())  
box = []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    box.append(tmp)

dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

def bfs():
    queue = deque()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x] == 1:
                    queue.append((z, y, x, 0))  
    
    max_day = 0
    
    while queue:
        z, y, x, day = queue.popleft()
        max_day = max(max_day, day)
        
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = 1
                    queue.append((nz, ny, nx, day + 1))
    
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z][y][x] == 0:
                    return -1  
    
    return max_day

result = bfs()
print(result)