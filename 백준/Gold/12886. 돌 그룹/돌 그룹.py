from collections import deque

A, B, C = map(int, input().split())

total = A+B+C

def bfs():
    visited = [[False] * total for _ in range(total)]

    q = deque()
    q.append((A, B))
    visited[A][B] = True
    while q:
        a, b = q.popleft()
        c = total - (a + b)
        if a == b == c:
            return 1
        for X, Y in [(a, b), (a, c), (b, c)]:
            if X == Y:
                continue
            if X > Y:
                X, Y = Y, X

            X, Y = X + X, Y - X
            mn = min(X, Y, total - (X + Y))
            mx = max(X, Y, total - (X + Y))
            if visited[mn][mx]:
                continue
            q.append((mn, mx))
            visited[mn][mx] = True
    return 0

if total % 3 != 0:
    print(0)
else:
   print(bfs())