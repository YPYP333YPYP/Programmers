from collections import deque

# 입력 받기
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 주사위 초기 상태 (위, 북, 동, 서, 남, 아래) 
dice = [1, 2, 3, 4, 5, 6]

# 방향 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 주사위 초기 위치와 방향
x, y = 0, 0  # 주사위 위치 (0, 0)부터 시작
dir = 0      # 초기 방향은 동쪽(0)

# 주사위 굴리기
def roll_dice(direction):
    global dice
    # 현재 주사위 상태
    top, north, east, west, south, bottom = dice
    
    # 방향에 따라 주사위 상태 변경
    if direction == 0:  # 동쪽
        dice = [west, north, top, bottom, south, east]
    elif direction == 1:  # 남쪽
        dice = [north, bottom, east, west, top, south]
    elif direction == 2:  # 서쪽
        dice = [east, north, bottom, top, south, west]
    elif direction == 3:  # 북쪽
        dice = [south, top, east, west, bottom, north]

# BFS로 점수 계산하기
def calculate_score(r, c):
    value = board[r][c]  # 현재 칸의 값
    count = 1            # 현재 칸도 포함
    visited = [[False] * M for _ in range(N)]
    visited[r][c] = True
    queue = deque([(r, c)])
    
    while queue:
        cr, cc = queue.popleft()
        
        for i in range(4):
            nr, nc = cr + dx[i], cc + dy[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and board[nr][nc] == value:
                visited[nr][nc] = True
                queue.append((nr, nc))
                count += 1
    
    return count * value

# 게임 시작
total_score = 0

for _ in range(K):
    # 1. 주사위 이동 방향으로 한 칸 굴러감
    nx, ny = x + dx[dir], y + dy[dir]
    
    # 칸이 없다면 이동 방향을 반대로 바꾸고 한 칸 굴러감
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        dir = (dir + 2) % 4
        nx, ny = x + dx[dir], y + dy[dir]
    
    # 주사위 위치 업데이트
    x, y = nx, ny
    
    # 주사위 굴리기
    roll_dice(dir)
    
    # 2. 도착한 칸에 대한 점수 획득
    total_score += calculate_score(x, y)
    
    # 3. 이동 방향 결정
    # A: 주사위 아랫면의 정수
    # B: 주사위가 있는 칸의 정수
    A = dice[5]  # 주사위 아랫면
    B = board[x][y]  # 현재 칸
    
    if A > B:
        dir = (dir + 1) % 4  # 시계 방향 90도 회전
    elif A < B:
        dir = (dir - 1) % 4  # 반시계 방향 90도 회전
    # A == B인 경우 방향 변화 없음

# 획득한 점수의 합
print(total_score)