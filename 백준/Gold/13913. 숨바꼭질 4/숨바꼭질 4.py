from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001
parent = [-1] * 100001  


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        x = q.popleft()

        if x == K:
            path = []
            current = x
            while current != -1:
                path.append(current)
                current = parent[current]
            return len(path) - 1, path[::-1]

        for next_x in [x - 1, x + 1, x * 2]:
            if 0 <= next_x <= 100000 and not visited[next_x]:
                visited[next_x] = True
                parent[next_x] = x  
                q.append(next_x)


time, path = bfs(N)
print(time)
print(*path)