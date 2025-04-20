N = int(input())
costs = []

for _ in range(N):
    costs.append(list(map(int, input().split())))

# dp[i][j]: i번 집까지 칠했을 때, i번 집을 j색으로 칠했을 때의 최소 비용
dp = [[0 for _ in range(3)] for _ in range(N)]

dp[0][0] = costs[0][0]  # 빨강
dp[0][1] = costs[0][1]  # 초록
dp[0][2] = costs[0][2]  # 파랑

for i in range(1, N):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
    
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
    
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

# 최소 비용 출력
result = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
print(result)