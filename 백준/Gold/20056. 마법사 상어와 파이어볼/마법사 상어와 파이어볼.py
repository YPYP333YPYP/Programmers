import sys

input = sys.stdin.readline

# 방향 배열 (북쪽부터 시계방향)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireball_info = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball_info.append([r, c, m, s, d])  # 행, 열, 질량, 속력, 방향


def move_fireballs():
    # 모든 파이어볼이 이동한 후의 위치를 저장
    positions = set()  # 파이어볼이 있는 위치 집합
    temp = [[[] for _ in range(N + 1)] for _ in range(N + 1)]  # 각 위치별 파이어볼 정보

    # 모든 파이어볼 이동
    while fireball_info:
        r, c, m, s, d = fireball_info.pop()

        # 속력만큼 이동
        nr = r + dx[d] * s
        nc = c + dy[d] * s

        # 1~N 범위를 벗어나면 처리
        nr = adjust_position(nr)
        nc = adjust_position(nc)

        # 새 위치에 파이어볼 추가
        positions.add((nr, nc))
        temp[nr][nc].append((m, s, d))

    # 2개 이상 파이어볼이 있는 칸 처리
    handle_multiple_fireballs(positions, temp)


def adjust_position(pos):
    # 1~N 범위로 좌표 조정
    if 1 <= pos <= N:
        return pos

    # 1보다 작으면
    if pos < 1:
        return ((pos - 1) % N) + 1

    # N보다 크면
    return (pos - 1) % N + 1


def handle_multiple_fireballs(positions, temp):
    for r, c in positions:
        # 파이어볼이 1개면 그대로 추가
        if len(temp[r][c]) == 1:
            m, s, d = temp[r][c][0]
            fireball_info.append([r, c, m, s, d])
            continue

        # 파이어볼이 2개 이상인 경우
        total_count = len(temp[r][c])
        total_mass = 0
        total_speed = 0
        directions = []

        for m, s, d in temp[r][c]:
            total_mass += m
            total_speed += s
            directions.append(d)

        # 새 질량 계산
        new_mass = total_mass // 5
        if new_mass == 0:  # 질량이 0이면 소멸
            continue

        # 새 속력 계산
        new_speed = total_speed // total_count

        # 방향 결정 (모두 홀수이거나 모두 짝수인지 확인)
        even_count = 0
        odd_count = 0
        for d in directions:
            if d % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        # 새 파이어볼 생성
        if even_count == 0 or odd_count == 0:  # 모두 홀수이거나 모두 짝수
            for nd in [0, 2, 4, 6]:
                fireball_info.append([r, c, new_mass, new_speed, nd])
        else:  # 홀수, 짝수 섞여 있음
            for nd in [1, 3, 5, 7]:
                fireball_info.append([r, c, new_mass, new_speed, nd])


# K번 명령 실행
for _ in range(K):
    move_fireballs()

# 남은 파이어볼 질량 합 계산
result = sum(m for _, _, m, _, _ in fireball_info)
print(result)