ir = input()
stack = []
cnt = 0

for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else:
        if ir[i-1] == "(":  # 레이저인 경우
            stack.pop()
            cnt += len(stack)  # 현재의 쇠막대기들을 카운팅
        else:  # 쇠막대기 끝인 경우
            stack.pop()
            cnt += 1  # 나머지 부분을 세는 것

print(cnt)
