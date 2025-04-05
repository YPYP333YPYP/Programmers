from collections import deque

n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_ice_chunks():
    visited = [[False] * m for _ in range(n)]
    chunk_count = 0
    
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0 and not visited[i][j]:
                chunk_count += 1
                bfs(i, j, visited)
                if chunk_count >= 2:
                    return chunk_count
    
    return chunk_count

def melt_ice():
    melt_amount = [[0] * m for _ in range(n)]
    ice_left = False
    
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and ice[nx][ny] == 0:
                        melt_amount[i][j] += 1
    
    for i in range(n):
        for j in range(m):
            if ice[i][j] > 0:
                ice[i][j] = max(0, ice[i][j] - melt_amount[i][j])
                if ice[i][j] > 0:
                    ice_left = True
    
    return not ice_left

time = 0

initial_chunks = count_ice_chunks()
if initial_chunks == 0:
    print(0)
    exit()

while True:
    time += 1
    all_melted = melt_ice()
    
    if all_melted:
        print(0)
        break
    
    chunks = count_ice_chunks()
    
    if chunks >= 2:
        print(time)
        break