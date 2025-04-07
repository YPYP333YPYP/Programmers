def angler(i, sharks, R):
    # 현재 열에서 가장 위에 있는 상어 찾기
    targets = [(r, idx) for idx, (r, c, _, _, _) in enumerate(sharks) if c == i+1]
    if not targets:
        return 0
    # 가장 위에 있는 상어 잡기
    min_row, idx = min(targets)
    size = sharks[idx][4]
    sharks.pop(idx)
    return size

def move_sharks(sharks, R, C):
    positions = {}
    
    for r, c, s, d, z in sharks:
        # 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
        
        # 위, 아래 방향 처리
        if d <= 2:
            # 방향 이동 주기 (R이 1인 경우 처리)
            cycle = 2 * (R - 1) if R > 1 else 1
            s %= cycle
            
            # 현재 위치와 방향 기준으로 이동
            if d == 1:  # 위로 이동 중
                r -= s
                if r < 1:  # 위쪽 경계를 넘어감
                    r = 2 - r  # 반사
                    d = 2  # 방향 전환
                if r > R:  # 한 번 더 반사될 수 있음
                    r = 2 * R - r
                    d = 1
            else:  # 아래로 이동 중
                r += s
                if r > R:  # 아래쪽 경계를 넘어감
                    r = 2 * R - r  # 반사
                    d = 1  # 방향 전환
                if r < 1:  # 한 번 더 반사될 수 있음
                    r = 2 - r
                    d = 2
        
        # 좌, 우 방향 처리
        else:
            # 방향 이동 주기 (C가 1인 경우 처리)
            cycle = 2 * (C - 1) if C > 1 else 1
            s %= cycle
            
            # 현재 위치와 방향 기준으로 이동
            if d == 4:  # 왼쪽으로 이동 중
                c -= s
                if c < 1:  # 왼쪽 경계를 넘어감
                    c = 2 - c  # 반사
                    d = 3  # 방향 전환
                if c > C:  # 한 번 더 반사될 수 있음
                    c = 2 * C - c
                    d = 4
            else:  # 오른쪽으로 이동 중
                c += s
                if c > C:  # 오른쪽 경계를 넘어감
                    c = 2 * C - c  # 반사
                    d = 4  # 방향 전환
                if c < 1:  # 한 번 더 반사될 수 있음
                    c = 2 - c
                    d = 3
        
        # 크기가 큰 상어만 남기기
        pos = (r, c)
        if pos not in positions or z > positions[pos][4]:
            positions[pos] = [r, c, s, d, z]
    
    return list(positions.values())

# 메인 코드
R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]

total = 0
for i in range(C):
    total += angler(i, sharks, R)
    if not sharks:
        break
    sharks = move_sharks(sharks, R, C)

print(total)