from collections import deque

# 입력 받기
N, M = map(int, input().split())
lab = []
viruses = []  # 바이러스 위치 저장
empty_count = 0  # 빈 칸의 개수 (바이러스를 퍼뜨려야 하는 칸)

for i in range(N):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(N):
        if row[j] == 2:  # 바이러스
            viruses.append((i, j))
        elif row[j] == 0:  # 빈 칸
            empty_count += 1

# 빈 칸이 없으면 바로 0 출력하고 종료
if empty_count == 0:
    print(0)
    exit(0)

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def combinations(arr, r):
    """
    arr에서 r개를 선택하는 모든 조합을 생성하는 함수
    """
    result = []
    
    def backtrack(start, combo):
        if len(combo) == r:
            result.append(combo[:])
            return
        
        for i in range(start, len(arr)):
            combo.append(arr[i])
            backtrack(i + 1, combo)
            combo.pop()
    
    backtrack(0, [])
    return result

def spread_virus(active_viruses):
    """
    활성화된 바이러스로부터 바이러스를 퍼뜨리고 모든 빈 칸이 바이러스로 채워지는 최소 시간 반환
    빈 칸을 모두 채울 수 없는 경우 -1 반환
    """
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    
    # 활성화된 바이러스의 위치를 큐에 넣고 방문 표시
    for x, y in active_viruses:
        queue.append((x, y))
        visited[x][y] = 0
    
    filled_count = 0  # 바이러스가 퍼진 빈 칸의 개수
    max_time = 0  # 모든 빈 칸에 바이러스가 퍼지는 데 걸리는 시간
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 내에 있고 아직 방문하지 않은 칸
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 벽이 아닌 경우
                if lab[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    
                    # 빈 칸인 경우 (원래 바이러스가 있던 곳이 아닌 경우)
                    if lab[nx][ny] == 0:
                        filled_count += 1
                        max_time = max(max_time, visited[nx][ny])
    
    # 모든 빈 칸이 바이러스로 채워졌는지 확인
    if filled_count == empty_count:
        return max_time
    else:
        return float('inf')  # 채울 수 없는 경우 무한대 반환

# M개의 바이러스를 활성화시키는 모든 조합에 대해 시뮬레이션
min_time = float('inf')
for active_viruses in combinations(viruses, M):
    time = spread_virus(active_viruses)
    min_time = min(min_time, time)

print(min_time if min_time != float('inf') else -1)