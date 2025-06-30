n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 방향: 0=왼쪽아래, 1=아래, 2=오른쪽아래
# dp[행][열][마지막방향] = 그 위치에 그 방향으로 도착한 최소비용
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

# 첫 번째 행 초기화 (어떤 방향으로든 시작 가능)
for j in range(m):
    for direction in range(3):
        dp[0][j][direction] = grid[0][j]

# 각 행을 순서대로 처리
for row in range(n - 1):
    for col in range(m):
        for last_dir in range(3):
            # 현재 위치에 도달할 수 없다면 건너뛰기
            if dp[row][col][last_dir] == float('inf'):
                continue
            
            current_cost = dp[row][col][last_dir]
            
            # 1. 왼쪽 아래로 이동 (방향 0)
            if col > 0 and last_dir != 0:  # 경계 체크 + 연속 같은 방향 방지
                new_cost = current_cost + grid[row + 1][col - 1]
                dp[row + 1][col - 1][0] = min(dp[row + 1][col - 1][0], new_cost)
            
            # 2. 바로 아래로 이동 (방향 1)
            if last_dir != 1:  # 연속 같은 방향 방지
                new_cost = current_cost + grid[row + 1][col]
                dp[row + 1][col][1] = min(dp[row + 1][col][1], new_cost)
            
            # 3. 오른쪽 아래로 이동 (방향 2)
            if col < m - 1 and last_dir != 2:  # 경계 체크 + 연속 같은 방향 방지
                new_cost = current_cost + grid[row + 1][col + 1]
                dp[row + 1][col + 1][2] = min(dp[row + 1][col + 1][2], new_cost)

# 마지막 행에서 최솟값 찾기
answer = float('inf')
for j in range(m):
    for direction in range(3):
        answer = min(answer, dp[n - 1][j][direction])

print(answer)