from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001


def bfs(value):
    q = deque()
    q.append((value, 0))
    visited[value] = True

    while q:
        x, t = q.popleft()

        if x == K:
            return t

        if x * 2 <= 100000 and not visited[x * 2]:
            visited[x * 2] = True
            q.appendleft((x * 2, t)) 

        if x - 1 >= 0 and not visited[x - 1]:
            visited[x - 1] = True
            q.append((x - 1, t + 1))

        if x + 1 <= 100000 and not visited[x + 1]:
            visited[x + 1] = True
            q.append((x + 1, t + 1))


print(bfs(N))