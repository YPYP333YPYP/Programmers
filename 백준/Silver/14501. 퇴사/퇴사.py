N = int(input())
T = []  # 상담에 걸리는 시간
P = []  # 상담 시 받는 금액

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp[i] = i일부터 가능한 최대 수익
dp = [0] * (N + 1)

# 뒤에서부터 계산
for i in range(N - 1, -1, -1):
    # i일에 상담을 하는 경우, 끝나는 날이 퇴사일을 넘어가면 상담 불가능
    if i + T[i] > N:
        dp[i] = dp[i + 1]  # i일에 상담을 하지 않는 경우와 같음
    else:
        # 상담을 하는 경우와 하지 않는 경우 중 최대 수익 선택
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

# 결과 출력
print(dp[0])