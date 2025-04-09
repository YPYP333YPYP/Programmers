from collections import deque

# 입력 받기
board_size, horse_count = map(int, input().split())
# 0: 흰색, 1: 빨간색, 2: 파란색
board = [list(map(int, input().split())) for _ in range(board_size)]

# 각 칸에 쌓인 말들의 정보
board_state = [[[] for _ in range(board_size)] for _ in range(board_size)]

# 방향 벡터: 우(동), 좌(서), 상(북), 하(남)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 말들의 정보 저장
horses = []
for i in range(horse_count):
    # 1-indexed를 0-indexed로 변환
    x, y, direction = map(int, input().split())
    x -= 1
    y -= 1
    direction -= 1
    horses.append([x, y, direction])
    board_state[x][y].append(i)  # 말의 번호를 저장

# 반대 방향으로 변경
def reverse_direction(direction):
    return {0: 1, 1: 0, 2: 3, 3: 2}[direction]

# 한 턴에 말 이동 수행
def move_horse(horse_idx):
    # 현재 말의 정보
    x, y, direction = horses[horse_idx]
    
    # 다음 위치 계산
    nx, ny = x + directions[direction][0], y + directions[direction][1]
    
    # 파란색 칸이거나 체스판 밖인 경우
    if not (0 <= nx < board_size and 0 <= ny < board_size) or board[nx][ny] == 2:
        # 방향 전환
        direction = reverse_direction(direction)
        horses[horse_idx][2] = direction
        
        # 새 방향으로 이동할 위치 계산
        nx, ny = x + directions[direction][0], y + directions[direction][1]
        
        # 또 파란색이거나 체스판 밖이면 이동 안 함
        if not (0 <= nx < board_size and 0 <= ny < board_size) or board[nx][ny] == 2:
            return True  # 계속 진행
    
    # 현재 위치에서 이동시킬 말들 (현재 말부터 위에 있는 모든 말)
    moving_horses = []
    for idx, h in enumerate(board_state[x][y]):
        if h == horse_idx:  # 현재 말부터
            moving_horses = board_state[x][y][idx:]
            board_state[x][y] = board_state[x][y][:idx]  # 남은 말들
            break
    
    # 빨간색 칸이면 순서 뒤집기
    if board[nx][ny] == 1:
        moving_horses.reverse()
    
    # 말들을 새 위치로 이동
    for h in moving_horses:
        horses[h][0], horses[h][1] = nx, ny  # 말의 위치 업데이트
        board_state[nx][ny].append(h)  # 새 위치에 말 추가
    
    # 말이 4개 이상 쌓이면 게임 종료
    if len(board_state[nx][ny]) >= 4:
        return False  # 게임 종료
    
    return True  # 계속 진행

# 게임 시작
turn_count = 0
while True:
    # 1000턴이 넘으면 게임 종료
    if turn_count > 1000:
        print(-1)
        break
    
    turn_count += 1
    game_over = False
    
    # 모든 말에 대해 이동 수행
    for i in range(horse_count):
        if not move_horse(i):  # 게임 종료 조건 충족
            game_over = True
            break
    
    # 게임이 종료되었으면 현재 턴 출력 후 종료
    if game_over:
        print(turn_count)
        break