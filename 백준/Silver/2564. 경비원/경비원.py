from collections import deque

x, y = map(int, input().split())
n = int(input())
loc = [list(map(int, input().split())) for _ in range(n)]
d,l = map(int, input().split())

graph = [[False] * x] +[[False] + [True] * (x-1) + [False] for _ in range(y-1)] + [[False] * x]

start = set()
if d == 1:
    start = (0,l)
elif d == 2:
    start = (y,l)
elif d == 3:
    start = (l,0)
else:
    start = (l,x)

def bfs(a,b):
    visited = [[False] * (x+1)] +[[False] + [True] * (x-1) + [False] for _ in range(y-1)] + [[False] * (x+1)]
    if a == 1:
        lx,ly = (0,b)
    elif a == 2:
        lx,ly = (y,b)
    elif a == 3:
        lx,ly = (b,0)
    else:
        lx,ly = (b,x)

    q = deque()
    sx,sy = start
    q.append((lx,ly,0))
    visited[lx][ly] = True


    while q:
        i, j, cnt = q.popleft()

        if sx == i and sy == j:
            return cnt

        for dx ,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = i+dx, j+dy

            if 0 <= nx <= y and 0<= ny <= x and not visited[nx][ny]:
                q.append((nx,ny,cnt+1))
                visited[nx][ny] = True

result = 0
for l in loc:
    a,b = l
    result += bfs(a,b)

print(result)
