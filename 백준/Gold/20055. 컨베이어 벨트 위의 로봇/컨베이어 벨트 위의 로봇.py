n, k = map(int, input().split())

belt = list(map(int, input().split()))
robot = [False] * (2 * n)


# 회전
def rotate():
    # 벨트 회전
    belt.insert(0, belt.pop())
    # 로봇 회전
    robot.insert(0, robot.pop())
    # 내리는 위치에 로봇이 있다면 내림
    if robot[n - 1]:
        robot[n - 1] = False


def move_robots():
    # 가장 먼저 벨트에 올라간 로봇부터 이동 (n-2부터 0까지 역순)
    for i in range(n - 2, -1, -1):
        # 현재 위치에 로봇이 있고, 다음 위치에 로봇이 없으며, 다음 위치의 내구도가 1 이상인 경우
        if robot[i] and not robot[i + 1] and belt[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1

    # 내리는 위치에 로봇이 있다면 내림
    if robot[n - 1]:
        robot[n - 1] = False


def add_robot():
    # 올리는 위치에 로봇이 없고, 내구도가 1 이상이면 로봇 올림
    if not robot[0] and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1


def count_zero():
    # 내구도가 0인 칸의 개수
    return belt.count(0)


# 시뮬레이션 시작
step = 0

while True:
    step += 1

    # 1. 벨트와 로봇 회전
    rotate()

    # 2. 로봇 이동
    move_robots()

    # 3. 로봇 올리기
    add_robot()

    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 종료
    if count_zero() >= k:
        break

print(step)