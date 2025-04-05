import sys

# 입력 받기
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))  # [+, -, *, /] 각각의 개수

# 최대값과 최소값 초기화
max_result = -1000000000
min_result = 1000000000

# DFS 함수 정의
def dfs(depth, result):
    global max_result, min_result, operators
    
    if depth == n - 1:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    # 각 연산자에 대해 시도
    for i in range(4):
        # 해당 연산자가 남아있는 경우
        if operators[i] > 0:
            # 연산자 사용
            operators[i] -= 1
            
            new_result = result
            # 연산 수행
            if i == 0:      # 덧셈
                new_result += numbers[depth + 1]
            elif i == 1:    # 뺄셈
                new_result -= numbers[depth + 1]
            elif i == 2:    # 곱셈
                new_result *= numbers[depth + 1]
            else:           # 나눗셈
                # 음수를 양수로 나누는 경우 처리
                if new_result < 0:
                    new_result = -(-new_result // numbers[depth + 1])
                else:
                    new_result //= numbers[depth + 1]
            
            # 다음 단계 탐색
            dfs(depth + 1, new_result)
            
            # 백트래킹 (연산자 반환)
            operators[i] += 1

dfs(0, numbers[0])

print(max_result)
print(min_result)