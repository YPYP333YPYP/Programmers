from collections import deque

def bfs(x, y, height, graph, visited, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        curr_x, curr_y = queue.popleft()
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_safe_areas(graph, height, n):
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > height:
                bfs(i, j, height, graph, visited, n)
                count += 1
    
    return count


n = int(input())
graph = []

min_height = 101 
max_height = 0    

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

    min_height = min(min_height, min(row))
    max_height = max(max_height, max(row))

    max_safe_areas = 0

for height in range(0, max_height):
    safe_areas = count_safe_areas(graph, height, n)
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)