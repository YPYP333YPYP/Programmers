from collections import deque

def bfs(maps, start_x, start_y, visited):
    queue = deque()
    visited[start_x][start_y] = 1
    queue.append((start_x,start_y))
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <= len(maps) - 1 and  0 <= ny <= len(maps[0])-1:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    maps[nx][ny] = 1 + maps[x][y]
                    queue.append((nx,ny))
                    
    return maps[len(maps)-1][len(maps[0])-1]           
def solution(maps):
    
    row = len(maps[0])
    col = len(maps)
    
    visited = [[0] * row for x in range(col)]
    result = bfs(maps,0,0,visited)
    return -1 if result == 1 else result