n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cloud_move_list = [list(map(int, input().split())) for _ in range(m)]

# 초기 구름 위치
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

# 8방향: ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향 (↖, ↗, ↘, ↙)
diag_dirs = [1, 3, 5, 7]

def move_clouds(d, s):
    # 방향 인덱스 조정 (1-indexed -> 0-indexed)
    d -= 1
    # 이동 거리 최적화 (n번 이동은 0번 이동과 동일)
    s = s % n
    
    new_clouds = []
    for x, y in clouds:
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        new_clouds.append((nx, ny))
    
    return new_clouds

def water_copy_bug():
    # 구름이 있는 칸의 물 +1
    for x, y in clouds:
        graph[x][y] += 1
    
    # 물복사버그 마법 수행
    for x, y in clouds:
        count = 0
        for dir in diag_dirs:
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > 0:
                count += 1
        graph[x][y] += count

def create_new_clouds():
    # 구름이 사라진 칸 표시
    cloud_positions = set(clouds)
    
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and (i, j) not in cloud_positions:
                new_clouds.append((i, j))
                graph[i][j] -= 2
    
    return new_clouds

# 메인 로직
for d, s in cloud_move_list:
    # 1. 구름 이동
    clouds = move_clouds(d, s)
    
    # 2. 비 내리기 & 물복사버그 마법
    water_copy_bug()
    
    # 3. 새로운 구름 생성
    clouds = create_new_clouds()

# 물의 양 합계 계산
total_water = sum(sum(row) for row in graph)
print(total_water)