from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def sol(s):
    global visited
    q = deque()
    visited[s] = True
    q.append(s)

    while q:
        x = q.popleft()

        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)


result = 0
for i in range(1,N+1):
    if not visited[i]:
        sol(i)
        result +=1

print(result)
