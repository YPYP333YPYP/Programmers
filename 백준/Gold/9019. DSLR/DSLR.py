from collections import deque


def bfs(start, end):
    queue = deque([(start, "")])
    visited = [False] * 10000
    visited[start] = True

    while queue:
        num, commands = queue.popleft()

        if num == end:
            return commands

        # D 연산: 2n mod 10000
        d_num = (num * 2) % 10000
        if not visited[d_num]:
            visited[d_num] = True
            queue.append((d_num, commands + "D"))

        # S 연산: n-1 (0이면 9999)
        s_num = num - 1 if num > 0 else 9999
        if not visited[s_num]:
            visited[s_num] = True
            queue.append((s_num, commands + "S"))

        # L 연산: 왼쪽으로 자릿수 회전
        l_num = (num % 1000) * 10 + num // 1000
        if not visited[l_num]:
            visited[l_num] = True
            queue.append((l_num, commands + "L"))

        # R 연산: 오른쪽으로 자릿수 회전
        r_num = (num % 10) * 1000 + num // 10
        if not visited[r_num]:
            visited[r_num] = True
            queue.append((r_num, commands + "R"))


T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    print(bfs(start, end))