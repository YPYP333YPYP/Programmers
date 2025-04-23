from collections import deque

start, end = map(int, input().split())




def bfs(start):
    q = deque()
    visited = set()
    visited.add(start)
    q.append((start,""))
    MAX = 10e9

    while q:
        n, c = q.popleft()

        if n == end:
            return c

        nv = n*n
        if 0<= nv < MAX and nv not in visited:
            visited.add(nv)
            q.append((nv, c+"*"))

        nv = n+n
        if 0 <= nv < MAX and nv not in visited:
            visited.add(nv)
            q.append((nv, c + "+"))

        nv = 1
        if nv not in visited:
            visited.add(nv)
            q.append((nv, c+"/"))
    return -1

if start == end:
    print(0)
else:
    print(bfs(start))