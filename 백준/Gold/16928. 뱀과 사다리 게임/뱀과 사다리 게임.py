from collections import deque

A, B = map(int, input().split())

snake_s = []
snake_e = []
ladder_s = []
ladder_e = []

for _ in range(A):
    x, y = map(int, input().split())
    ladder_s.append(x)
    ladder_e.append(y)


for _ in range(B):
    x, y = map(int, input().split())
    snake_s.append(x)
    snake_e.append(y)



def bfs():
    visited = [False] * 101
    q = deque()
    q.append((1,0))
    visited[1] = True

    while q:
        x,c = q.popleft()

        if x == 100:
            return c

        for dx in range(1,7):
            nx = x + dx
            if 0 <= nx <= 100 and not visited[nx]:
                visited[nx] = True
                if nx in ladder_s:
                    idx = ladder_s.index(nx)
                    nv = ladder_e[idx]
                    visited[nv] = True
                    q.append((nv,c+1))
                elif nx in snake_s:
                    idx = snake_s.index(nx)
                    nv = snake_e[idx]
                    visited[nv] = True
                    q.append((nv,c+1))
                else:
                    q.append((nx,c+1))

print(bfs())