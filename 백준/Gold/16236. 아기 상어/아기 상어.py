from collections import deque
time = 0
n = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    graph.append(list(map(int, input().split())))
shark_pos = (0, 0)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_pos = (i,j)
shark_size = 2
graph[shark_pos[0]][shark_pos[1]] = 0
def can_eat(sx, sy, ss):
    min_d = 10000
    q = deque()
    q.append((sx,sy,0))
    can_eat_list = []
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True
    
    while q:
        x,y,d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                
                if graph[nx][ny] <= ss:
                    q.append((nx, ny, d+1))
                    if 0 < graph[nx][ny] < ss:
                        if min_d >= d+1:
                            can_eat_list.append((nx, ny, d+1))
                            min_d = d+1
    if can_eat_list:
        can_eat_list.sort(key=lambda x:(x[2], x[0], x[1]))
        return can_eat_list[0]
    else:
        return [-1,-1,-1]
        
cnt = 0
while True:
    result = can_eat(shark_pos[0], shark_pos[1], shark_size)
    if result[0] == -1:
        break
    shark_pos = (result[0], result[1])
    time += result[2]
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
    graph[shark_pos[0]][shark_pos[1]] = 0
print(time)