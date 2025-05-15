N = int(input())

graph = [[] for _ in range(N)]
for i in range(N):
    row = input()
    for v in row:
        graph[i].append(v)

body = []


# 머리 찾기
def find_heart():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == '*':
                return (i+2, j+1)
    return None


heart = find_heart()

def find_body_length(heart_loc):
    y,x = heart_loc
    y,x = y-1, x-1

    # 왼쪽, 위, 오른쪽, 아래
    dy = [0,-1,0,1]
    dx = [-1,0,1,0]

    # 왼쪽 팔
    la = 0
    for i in range(1,N):
        nx = x + dx[0] * i
        if 0 <= nx < N:
            if graph[y][nx] == '*':
                la += 1
            else:
                break
        else:
            break

    # 오른쪽 팔
    ra = 0
    for i in range(1, N):
        nx = x + dx[2] * i
        if 0 <= nx < N:
            if graph[y][nx] == '*':
                ra += 1
            else:
                break
        else:
            break

    # 허리
    h = 0
    for i in range(1, N):
        ny = y + dy[3] * i
        if 0 <= ny < N:
            if graph[ny][x] == '*':
                h += 1
            else:
                break
        else:
            break

    h_loc = y+h,x
    ll_start = h_loc[0] + 1, h_loc[1] - 1
    rl_start = h_loc[0] + 1, h_loc[1] + 1

    ll = 1
    y,x = ll_start
    for i in range(1, N):
        ny = y + dy[3] * i
        if 0 <= ny < N:
            if graph[ny][x] == '*':
                ll += 1
            else:
                break
        else:
            break

    rl = 1
    y,x = rl_start
    for i in range(1, N):
        ny = y + dy[3] * i
        if 0 <= ny < N:
            if graph[ny][x] == '*':
                rl += 1
            else:
                break
        else:
            break

    return [la,ra,h,ll,rl]

print(*heart, sep=" ")
result = find_body_length(heart)
print(*result, sep = " ")