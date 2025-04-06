n, m, h = map(int, input().split())

line = [[0] * (n+1) for _ in range(h+1)]

# 초기 가로선 설정
for _ in range(m):
    x, y = map(int, input().split())
    line[x][y] = 1       # 오른쪽으로 이동
    line[x][y+1] = -1    # 왼쪽으로 이동

def check(data):
    """모든 세로선이 자기 자신으로 도착하는지 확인"""
    for k in range(1, n+1):
        j = k  # 시작 위치
        for i in range(1, h+1):
            j += data[i][j]  # 현재 위치의 선 정보에 따라 이동
        if j != k:  # 도착한 위치가 시작 위치와 다르면 실패
            return False
    return True

def dfs(cnt, idx):
    """백트래킹으로 가로선 추가"""
    global min_cnt
    
    # 현재 상태에서 모든 세로선이 자기 자신으로 도착하는지 확인
    if check(line):
        min_cnt = min(min_cnt, cnt)
        return
    
    # 최대 3개까지만 추가 가능하거나 이미 더 좋은 해가 있으면 종료
    if cnt == 3 or min_cnt <= cnt:
        return
    
    # 가능한 모든 위치에 가로선 추가 시도
    for i in range(idx, length):
        r, c = grid[i]
        # 해당 위치와 오른쪽 위치에 모두 선이 없어야 추가 가능
        if not line[r][c] and not line[r][c+1]:
            # 가로선 추가
            line[r][c] = 1     # 오른쪽으로 이동
            line[r][c+1] = -1  # 왼쪽으로 이동
            
            # 다음 가로선 추가 시도 (i+1부터 탐색)
            dfs(cnt+1, i+1)
            
            # 백트래킹: 가로선 제거
            line[r][c] = 0
            line[r][c+1] = 0

grid = []
for i in range(1, h+1):
    for j in range(1, n):
        if not line[i][j] and not line[i][j+1]:
            grid.append((i, j))

length = len(grid)
min_cnt = float('inf')

# 백트래킹 시작
dfs(0, 0)

if min_cnt <= 3:
    print(min_cnt)
else:
    print(-1)