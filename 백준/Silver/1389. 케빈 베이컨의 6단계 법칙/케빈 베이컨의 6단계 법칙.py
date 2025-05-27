from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def sol(s,e):
    visited = [False] * (N+1)
    q = deque()
    visited[s] = True
    q.append((s,0))

    while q:
        x, cnt = q.popleft()

        if x == e:
            return cnt

        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                q.append((y,cnt+1))

result = []

for i in range(1,N+1):
    tmp = 0
    for j in range(1,N+1):
        if i != j:
            tmp += sol(i,j)
    result.append(tmp)

v = min(result)
print(result.index(v)+1)