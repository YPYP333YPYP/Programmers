def spread_dust(room, R, C):
    # 미세먼지 확산을 위한 임시 배열
    temp = [[0] * C for _ in range(R)]
    
    # 공기청정기 위치 복사
    for i in range(R):
        for j in range(C):
            if room[i][j] == -1:
                temp[i][j] = -1
    
    # 미세먼지 확산
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                # 현재 위치의 미세먼지 양
                dust = room[i][j]
                # 확산된 방향 개수
                spread_count = 0
                
                # 4방향으로 확산 시도
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    
                    # 범위 체크 및 공기청정기가 없는 위치인지 확인
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        temp[nx][ny] += dust // 5
                        spread_count += 1
                
                # 남은 미세먼지 양 계산
                temp[i][j] += dust - (dust // 5) * spread_count
    
    return temp

def operate_air_purifier(room, R, C, air_purifier):
    # 위쪽 공기청정기 순환 (반시계 방향)
    top = air_purifier[0]
    
    # 아래로 당기기
    for i in range(top - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    
    # 왼쪽으로 당기기
    for i in range(0, C - 1):
        room[0][i] = room[0][i + 1]
    
    # 위로 당기기
    for i in range(0, top):
        room[i][C - 1] = room[i + 1][C - 1]
    
    # 오른쪽으로 당기기
    for i in range(C - 1, 1, -1):
        room[top][i] = room[top][i - 1]
    
    # 공기청정기에서 나오는 바람은 미세먼지가 없음
    room[top][1] = 0
    
    # 아래쪽 공기청정기 순환 (시계 방향)
    bottom = air_purifier[1]
    
    # 위로 당기기
    for i in range(bottom + 1, R - 1):
        room[i][0] = room[i + 1][0]
    
    # 왼쪽으로 당기기
    for i in range(0, C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    
    # 아래로 당기기
    for i in range(R - 1, bottom, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    
    # 오른쪽으로 당기기
    for i in range(C - 1, 1, -1):
        room[bottom][i] = room[bottom][i - 1]
    
    # 공기청정기에서 나오는 바람은 미세먼지가 없음
    room[bottom][1] = 0

def solve():
    R, C, T = map(int, input().split())
    room = []
    air_purifier = []
    
    # 방 정보 입력 및 공기청정기 위치 저장
    for i in range(R):
        row = list(map(int, input().split()))
        room.append(row)
        if row[0] == -1:
            air_purifier.append(i)
    
    # T초 동안 시뮬레이션
    for _ in range(T):
        # 미세먼지 확산
        room = spread_dust(room, R, C)
        
        # 공기청정기 작동
        operate_air_purifier(room, R, C, air_purifier)
    
    # 남아 있는 미세먼지의 양 계산
    total_dust = 0
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                total_dust += room[i][j]
    
    return total_dust

print(solve())