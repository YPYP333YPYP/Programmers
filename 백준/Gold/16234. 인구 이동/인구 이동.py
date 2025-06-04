from collections import deque

N, L, R = map(int, input().split())

graph = []

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)



def bfs(x,y,v):
    queue = deque()
    queue.append((x,y))
    v[x][y] = True
    union = []
    union.append((x,y))

    while queue:
        x,y = queue.popleft()

        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and ( L <= abs(graph[nx][ny] - graph[x][y]) <= R) and not v[nx][ny]:
                queue.append((nx,ny))
                v[nx][ny] = True
                union.append((nx,ny))

    if len(union) > 1:
        return union
    else:
        return False


def check():
    visited = [[False for _ in range(N)] for _ in range(N)]
    u = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = bfs(i,j,visited)
                if result:
                    u.append(result)
    return u

def share(arr):
    for tmp in arr:
        calc = sum([graph[x][y] for x,y in tmp])
        avg = calc//len(tmp)


        for x,y in tmp:
            graph[x][y] = avg

i = 0
while True:
    tmp = check()
    if len(tmp) == 0:
        break
    else:
        share(tmp)
        i+=1

print(i)