n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 방향: 좌, 하, 우, 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 각 방향별 모래 퍼짐 패턴 (x위치, y위치, 비율)
wind = [
    [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (1, 1, 0.01),
     (-1, 1, 0.01)],
    [(2, 0, 0.05), (1, -1, 0.1), (1, 1, 0.1), (0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), (0, -1, 0.07), (-1, 1, 0.01),
     (-1, -1, 0.01)],
    [(0, 2, 0.05), (-1, 1, 0.1), (1, 1, 0.1), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.01),
     (1, -1, 0.01)],
    [(-2, 0, 0.05), (-1, -1, 0.1), (-1, 1, 0.1), (0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), (0, -1, 0.07), (1, 1, 0.01),
     (1, -1, 0.01)]]

# 격자 밖으로 나간 모래를 계산하는 방식으로 변경
out_sand = 0

def sand(x, y, d):
    global out_sand
    
    # 현재 위치의 모래양
    sand_amount = arr[x][y]
    arr[x][y] = 0
    
    # 분산된 모래 합계
    scattered = 0
    
    # 9개 방향으로 모래 분산
    for dx_offset, dy_offset, ratio in wind[d]:
        nx, ny = x + dx_offset, y + dy_offset
        move_sand = int(sand_amount * ratio)
        scattered += move_sand
        
        # 격자 내부인 경우
        if 0 <= nx < n and 0 <= ny < n:
            arr[nx][ny] += move_sand
        else:
            # 격자 밖으로 나간 모래
            out_sand += move_sand
    
    # 알파 위치 계산
    nx, ny = x + dx[d], y + dy[d]
    alpha_sand = sand_amount - scattered
    
    # 알파 위치가 격자 내부인 경우
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += alpha_sand
    else:
        out_sand += alpha_sand

# 토네이도 이동 거리 계산 (더 간결하게)
moves = []
for i in range(1, n):
    moves.extend([i, i])
moves.append(n-1)

# 시작 위치
x, y = n // 2, n // 2
d = 0

# 토네이도 이동
for distance in moves:
    for _ in range(distance):
        x += dx[d]
        y += dy[d]
        if arr[x][y] > 0:
            sand(x, y, d)
    d = (d + 1) % 4

print(out_sand)