N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_sum = 0

# 방문 배열
visited = [[False] * M for _ in range(N)]

def dfs(x, y, depth, total):
    global max_sum
    
    if total + (4-depth) * 1000 <= max_sum:  
        return
    
    if depth == 4:
        max_sum = max(max_sum, total)
        return
    
    # 상하좌우 방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        # 범위 체크 및 방문 여부 체크
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

def check_T_shape(x, y):
    global max_sum
    
    tetrominos = [
        # ㅜ 모양
        [(0,0), (0,1), (0,2), (1,1)],
        # ㅏ 모양
        [(0,0), (1,0), (2,0), (1,1)],
        # ㅗ 모양
        [(0,1), (1,0), (1,1), (1,2)],
        # ㅓ 모양
        [(0,1), (1,0), (1,1), (2,1)]
    ]
    
    for tetromino in tetrominos:
        total = 0
        flag = True
        
        for dx, dy in tetromino:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                flag = False
                break
                
            total += board[nx][ny]
            
        if flag:
            max_sum = max(max_sum, total)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        
        check_T_shape(i, j)

# 결과 출력
print(max_sum)