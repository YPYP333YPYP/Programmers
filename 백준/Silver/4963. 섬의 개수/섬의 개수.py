
def dfs(graph, x,y,visited,cnt):
    row, col = len(graph), len(graph[0])

    if (x < 0 or x >= row or y < 0 or y >= col or graph[x][y] == 0 or visited[x][y]):
        return

    visited[x][y] = True
    cnt += 1

    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]:
        nx,ny = x+dx, y+dy
        dfs(graph, nx, ny, visited,cnt)

    return cnt

while True:
    W,H = map(int,input().split())

    if W == 0 and H == 0:
        break
    cnt = 0
    graph = [list(map(int,input().split())) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt = dfs(graph,i,j,visited,cnt)
    print(cnt)