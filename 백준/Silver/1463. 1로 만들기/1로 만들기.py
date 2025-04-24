X = int(input())


def min_operations(n):
    dp = [0] * (n + 1)

    # 2부터 n까지 각 숫자에 대해 계산
    for i in range(2, n + 1):

        # 1) 1을 빼는 경우 (항상 가능)
        dp[i] = dp[i - 1] + 1

        # 2) 2로 나누는 경우 (i가 2의 배수일 때)
        if i % 2 == 0:
            # 현재값과 i/2를 1로 만드는 연산 횟수+1 중 최소값 선택
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3) 3으로 나누는 경우 (i가 3의 배수일 때)
        if i % 3 == 0:
            # 현재값과 i/3을 1로 만드는 연산 횟수+1 중 최소값 선택
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

print(min_operations(X))