from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 101 
    
    grid = [[0] * N for _ in range(N)]
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2, x2*2+1):
            for j in range(y1*2, y2*2+1):
                if i == x1*2 or i == x2*2 or j == y1*2 or j == y2*2:
                    grid[i][j] = 1
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2+1, x2*2):
            for j in range(y1*2+1, y2*2):
                grid[i][j] = 0
    
    # 방향 벡터
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    # BFS 함수
    def bfs(sx, sy, ex, ey):
        distance = [[0] * N for _ in range(N)]
        visited = [[False] * N for _ in range(N)]    
        
        q = deque()
        q.append((sx*2, sy*2))  # 좌표 2배 확대
        visited[sx*2][sy*2] = True
        
        while q:
            x, y = q.popleft()
            
            if x == ex*2 and y == ey*2:  
                return distance[x][y] // 2 
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
        
        return -1  
    
    answer = bfs(characterX, characterY, itemX, itemY)
    
    return answer