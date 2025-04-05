# 지도 크기, 주사위 초기 위치, 명령 개수 입력
n, m, x, y, k = map(int, input().split())

# 지도 정보 입력
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 이동 명령 입력
commands = list(map(int, input().split()))

# 이동 방향 정의 (동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 초기 상태 (위, 북, 동, 서, 남, 바닥)
dice = [0, 0, 0, 0, 0, 0]

# 주사위 굴리기 함수
def roll_dice(direction):
    global dice
    
    # 현재 주사위 상태 복사
    a, b, c, d, e, f = dice
    
    # 굴리는 방향에 따라 주사위 상태 업데이트
    if direction == 1:  # 동쪽
        dice = [d, b, a, f, e, c]
    elif direction == 2:  # 서쪽
        dice = [c, b, f, a, e, d]
    elif direction == 3:  # 북쪽
        dice = [e, a, c, d, f, b]
    else:  # 남쪽
        dice = [b, f, c, d, a, e]

# 명령 수행
for command in commands:
    # 이동할 위치 계산
    nx = x + dx[command-1]
    ny = y + dy[command-1]
    
    # 지도를 벗어나는 경우 명령 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    # 주사위 굴리기
    roll_dice(command)
    
    # 위치 업데이트
    x, y = nx, ny
    
    # 지도와 주사위 상호작용
    if board[x][y] == 0:
        # 칸의 값이 0이면 주사위 바닥면 값을 칸에 복사
        board[x][y] = dice[5]
    else:
        # 칸의 값이 0이 아니면 칸의 값을 주사위 바닥면에 복사, 칸은 0으로
        dice[5] = board[x][y]
        board[x][y] = 0
    
    # 주사위 윗면 출력
    print(dice[0])