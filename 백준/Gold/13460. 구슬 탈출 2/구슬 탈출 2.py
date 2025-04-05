from collections import deque
 
n, m = map(int, input().split()) 
 
board = [list(input().rstrip()) for _ in range(n)]
visited = []
 
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
 
def getPos():
    rx, ry, bx, by = 0, 0, 0, 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == "R":
                rx, ry = x, y
            if board[x][y] == "B":
                bx, by = x, y
    return rx, ry, bx, by
 
 
def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        cnt +=1
    return x, y, cnt
    
def bfs():
    rx, ry, bx, by = getPos()
 
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited.append((rx, ry, bx, by))
 
    while q:
        rx, ry, bx, by, result = q.popleft()
 
        if result > 10:
            break
 
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
 
            if board[nbx][nby] == "O":
                continue
 
            if board[nrx][nry] == "O":
                print(result)
                return
 
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
 
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, result + 1))
    print(-1)
 
bfs()