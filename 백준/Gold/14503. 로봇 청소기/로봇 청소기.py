n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # n개의 행 입력

result = 0

# 북, 동, 남, 서 방향으로 이동 (문제 정의에 맞게)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    # 1. 현재 칸이 청소되지 않은 경우, 청소
    if graph[r][c] == 0:
        graph[r][c] = 2  # 청소된 칸은 2로 표시
        result += 1

    # 2. 주변 4칸 확인
    cleaned = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:
            cleaned = False
            break

    if cleaned:  # 주변 4칸이 모두 청소되었거나 벽인 경우
        # 후진할 위치 계산
        back_r = r + dr[(d + 2) % 4]
        back_c = c + dc[(d + 2) % 4]

        # 후진할 수 없다면 작동 멈춤
        if back_r < 0 or back_r >= n or back_c < 0 or back_c >= m or graph[back_r][back_c] == 1:
            break

        # 후진
        r, c = back_r, back_c
    else:  # 청소되지 않은 칸이 있는 경우
        # 반시계 방향으로 90도 회전
        d = (d + 3) % 4

        # 앞쪽 칸이 청소되지 않은 빈칸인 경우 전진
        front_r = r + dr[d]
        front_c = c + dc[d]

        if 0 <= front_r < n and 0 <= front_c < m and graph[front_r][front_c] == 0:
            r, c = front_r, front_c

print(result)