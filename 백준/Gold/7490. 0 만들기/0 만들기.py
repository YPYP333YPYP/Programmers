def dfs(n, index, expression, current):
    # 기저 조건: 모든 숫자를 사용했을 때
    if index == n + 1:
        # 공백을 처리하고 계산
        calc_exp = expression.replace(' ', '')
        if eval(calc_exp) == 0:
            print(expression)
        return

    # 현재 숫자를 문자열로 변환
    num = str(index)

    # 공백 연산자 추가 (숫자 붙이기)
    if index > 1:  # 첫 번째 숫자에는 연산자를 붙이지 않음
        dfs(n, index + 1, expression + ' ' + num, current)

    # + 연산자 추가
    if index > 1:  # 첫 번째 숫자에는 연산자를 붙이지 않음
        dfs(n, index + 1, expression + '+' + num, current)

    # - 연산자 추가
    if index > 1:  # 첫 번째 숫자에는 연산자를 붙이지 않음
        dfs(n, index + 1, expression + '-' + num, current)

    # 첫 번째 숫자인 경우 (연산자 없음)
    if index == 1:
        dfs(n, index + 1, num, current)


def solve_problem():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        dfs(n, 1, "", 0)
        print()


solve_problem()