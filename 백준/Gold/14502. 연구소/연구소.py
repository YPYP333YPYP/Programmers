from collections import deque

n, m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

empty_spaces = []
virus_positions = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty_spaces.append((i, j))
        elif lab[i][j] == 2:
            virus_positions.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_virus():
    temp_lab = [row[:] for row in lab]
    
    for i, j in wall_positions:
        temp_lab[i][j] = 1
    
    queue = deque(virus_positions)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))
    
    safety_count = 0
    for i in range(n):
        for j in range(m):
            if temp_lab[i][j] == 0:
                safety_count += 1
    
    return safety_count

max_safety = 0

wall_positions = []

def select_walls(start, count):
    global max_safety
    
    if count == 3:
        safety = spread_virus()
        max_safety = max(max_safety, safety)
        return
    
    for i in range(start, len(empty_spaces)):
        wall_positions.append(empty_spaces[i])
        select_walls(i + 1, count + 1)
        wall_positions.pop()

select_walls(0, 0)

print(max_safety)