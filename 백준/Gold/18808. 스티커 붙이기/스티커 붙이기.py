# 노트북의 세로 크기 N, 가로 크기 M, 스티커의 개수 K
N, M, K = map(int, input().split())

# 노트북 상태 (0: 빈칸, 1: 스티커가 붙은 칸)
notebook = [[0] * M for _ in range(N)]

# 스티커들을 저장할 리스트
stickers = []

# 스티커 입력 받기
for _ in range(K):
    # 스티커의 세로 크기 R, 가로 크기 C
    R, C = map(int, input().split())
    
    # 스티커 정보 입력
    sticker_data = []
    for i in range(R):
        row = list(map(int, input().split()))
        sticker_data.append(row)
    
    # 스티커의 좌표 셋 생성
    sticker_coords = set()
    for i in range(R):
        for j in range(C):
            if sticker_data[i][j] == 1:
                sticker_coords.add((i, j))
    
    stickers.append((sticker_coords, R, C))

# 스티커를 회전시키는 함수
def rotate_sticker(sticker_info):
    coords, R, C = sticker_info
    new_coords = set()
    
    # 90도 회전 좌표 변환: (i, j) -> (j, R-1-i)
    for i, j in coords:
        new_coords.add((j, R-1-i))
    
    # 회전 후에는 R과 C가 서로 바뀜
    return (new_coords, C, R)

# 스티커를 노트북에 붙일 수 있는지 확인하는 함수
def can_attach(x, y, sticker_coords):
    for di, dj in sticker_coords:
        ni, nj = x + di, y + dj
        
        # 노트북 범위를 벗어나는지 확인
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            return False
        
        # 이미 스티커가 붙어있는지 확인
        if notebook[ni][nj] == 1:
            return False
    
    return True

# 스티커를 노트북에 붙이는 함수
def attach(x, y, sticker_coords):
    for di, dj in sticker_coords:
        notebook[x + di][y + dj] = 1

# 스티커를 노트북에 붙이는 과정 시뮬레이션
for sticker_info in stickers:
    sticker_coords, R, C = sticker_info
    attached = False
    
    # 0, 90, 180, 270도 회전 시도
    for _ in range(4):
        # 노트북의 모든 위치에서 시도
        for x in range(N):
            if attached:
                break
                
            for y in range(M):
                if can_attach(x, y, sticker_coords):
                    attach(x, y, sticker_coords)
                    attached = True
                    break
        
        # 스티커를 붙였으면 다음 스티커로 넘어감
        if attached:
            break
        
        # 스티커를 90도 회전
        sticker_info = rotate_sticker(sticker_info)
        sticker_coords, R, C = sticker_info

# 노트북에 붙은 스티커 칸의 개수 계산
result = sum(sum(row) for row in notebook)
print(result)