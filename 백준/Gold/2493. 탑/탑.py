N = int(input())
towers = list(map(int, input().split()))

stack = []
ans = [0] * N

for i in range(N):
    # 현재 탑보다 낮거나 같은 탑들을 스택에서 제거
    while stack:
        if stack[-1][1] > towers[i]:  # 스택 맨위가 현재보다 크면
            ans[i] = stack[-1][0] + 1  # 답 발견! (1-indexed)
            break
        else:
            stack.pop()  # 작거나 같으면 제거 (더 이상 쓸모없음)

    stack.append((i, towers[i]))  # 현재 탑을 스택에 추가

print(*ans)
