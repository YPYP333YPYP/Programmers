N, M = map(int, input().split())
office = []
cctvs = []

for i in range(N):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:  # CCTV인 경우
            cctvs.append((i, j, row[j])) 

# CCTV 감시 방향 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 종류별 감시 방향
# 1: 한 방향, 2: 양 방향(상하/좌우), 3: 직각 방향, 4: 세 방향, 5: 네 방향
cctv_directions = [
    [],
    [[0], [1], [2], [3]],  # 1번 CCTV
    [[0, 2], [1, 3]],  # 2번 CCTV
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번 CCTV
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번 CCTV
    [[0, 1, 2, 3]]  # 5번 CCTV
]

# 2차원 배열 복사 함수
def copy_array(arr):
    return [row[:] for row in arr]

# 감시 영역 표시 함수
def mark_watched(office, x, y, direction):
    N, M = len(office), len(office[0])
    result = copy_array(office)
    
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or result[nx][ny] == 6:
                break
            if result[nx][ny] == 0: 
                result[nx][ny] = -1
    
    return result

# DFS로 모든 CCTV 방향 조합 탐색
def dfs(office, cctvs, idx):
    # 모든 CCTV 방향을 결정한 경우
    if idx == len(cctvs):
        # 사각지대(0) 개수 세기
        blind_spot = 0
        for row in office:
            blind_spot += row.count(0)
        return blind_spot
    
    x, y, cctv_type = cctvs[idx]
    min_blind_spot = float('inf')
    
    # 현재 CCTV의 가능한 모든 방향 조합 탐색
    for direction in cctv_directions[cctv_type]:
        # 감시 영역 표시
        new_office = mark_watched(office, x, y, direction)
        # 다음 CCTV로 진행
        blind_spot = dfs(new_office, cctvs, idx + 1)
        min_blind_spot = min(min_blind_spot, blind_spot)
    
    return min_blind_spot


result = dfs(office, cctvs, 0)
print(result)