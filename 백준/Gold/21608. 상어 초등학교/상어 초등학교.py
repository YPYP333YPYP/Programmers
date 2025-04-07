
N = int(input())
students = []  # 학생 번호와 좋아하는 학생 목록 저장
for _ in range(N*N):
    info = list(map(int, input().split()))
    students.append((info[0], info[1:]))

# N x N 교실 초기화 (0은 빈 자리)
classroom = [[0] * N for _ in range(N)]

# 상하좌우 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 각 학생을 순서대로 배치
for student, likes in students:
    best_position = None
    max_like = -1
    max_empty = -1
    
    # 모든 빈 자리 확인
    for i in range(N):
        for j in range(N):
            if classroom[i][j] != 0:  # 이미 자리가 차있으면 건너뜀
                continue
                
            # 인접한 좋아하는 학생 수와 빈 칸 수 계산
            like_count = 0
            empty_count = 0
            
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                
                if 0 <= nx < N and 0 <= ny < N:
                    if classroom[nx][ny] in likes:  # 좋아하는 학생이 인접해 있는지
                        like_count += 1
                    elif classroom[nx][ny] == 0:  # 빈 칸이 인접해 있는지
                        empty_count += 1
            
            # 최적의 자리 업데이트
            if (like_count > max_like) or \
               (like_count == max_like and empty_count > max_empty) or \
               (like_count == max_like and empty_count == max_empty and \
                (best_position is None or i < best_position[0] or \
                 (i == best_position[0] and j < best_position[1]))):
                max_like = like_count
                max_empty = empty_count
                best_position = (i, j)
    
    # 최적의 자리에 학생 배치
    classroom[best_position[0]][best_position[1]] = student

# 만족도 계산
satisfaction = 0
student_likes = {}  # 학생별 좋아하는 학생 목록을 빠르게 조회하기 위한 딕셔너리
for student, likes in students:
    student_likes[student] = likes

for i in range(N):
    for j in range(N):
        student = classroom[i][j]
        like_count = 0
        
        # 인접한 좋아하는 학생 수 세기
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N and classroom[nx][ny] in student_likes[student]:
                like_count += 1
        
        # 만족도 계산 (0: 0, 1: 1, 2: 10, 3: 100, 4: 1000)
        if like_count > 0:
            satisfaction += 10 ** (like_count - 1)

print(satisfaction)