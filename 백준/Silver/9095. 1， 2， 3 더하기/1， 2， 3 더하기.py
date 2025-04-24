
def count_ways(n):
    # DP 배열 초기화
    dp = [0] * (n + 1)

    # 기저 사례 설정
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4

    # 점화식으로 dp 배열 채우기
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


# 테스트 케이스 수 입력
t = int(input())

# 각 테스트 케이스 처리
for _ in range(t):
    n = int(input())
    print(count_ways(n))

