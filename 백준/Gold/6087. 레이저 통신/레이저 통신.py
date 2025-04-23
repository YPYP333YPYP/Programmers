from collections import deque

# 입력 받기
W, H = map(int, input().split())
board = []
lasers = []

for i in range(H):
    row = input()
    board.append(row)
    for j, v in enumerate(row):
        if v == 'C':
            lasers.append((i, j))

# 방향: 동(0), 서(1), 남(2), 북(3)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    start, end = lasers
    
    # 거울 개수만 저장 (방향 정보는 저장하지 않음)
    dist = [[-1] * W for _ in range(H)]
    q = deque()
    
    # 시작점 초기화
    dist[start[0]][start[1]] = 0
    q.append(start)
    
    while q:
        x, y = q.popleft()
        
        # 목적지 도달 시 결과 반환
        if (x, y) == end:
            return dist[x][y]
        
        # 4방향 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            # 해당 방향으로 벽을 만나거나 경계를 벗어날 때까지 직진
            while 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*':
                # 아직 방문하지 않았거나, 더 적은 거울로 도달 가능한 경우
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # 이미 같은 거울 수로 방문한 경우 (중복 방문 방지)
                elif dist[nx][ny] == dist[x][y] + 1:
                    pass
                else:
                    break  # 더 많은 거울로 방문한 경우는 탐색 중단
                
                # 다음 칸으로 이동
                nx += dx[d]
                ny += dy[d]
    
    return -1  # 도달 불가능한 경우

result = bfs() - 1
print(result)