from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    choices = [0] + list(map(int, input().split()))

    # 팀을 이루지 못하는 학생 수
    no_team_count = n

    # 각 학생의 상태를 추적
    visited = [False] * (n + 1)
    in_team = [False] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue

        # 현재 탐색 경로에 포함된 학생들
        current_path = {}
        q = deque([(start, 0)])  # (학생 번호, 경로 상의 위치)

        while q:
            node, depth = q.popleft()

            if visited[node]:
                # 이미 방문한 노드를 다시 만났다면, 사이클이 존재할 가능성
                if node in current_path:
                    # 사이클 발견 - 해당 노드부터 현재 경로 끝까지가 팀을 이룸
                    cycle_start_depth = current_path[node]
                    cycle_size = depth - cycle_start_depth
                    no_team_count -= cycle_size

                    # 사이클에 속한 학생들은 팀을 이룸
                    for cycle_student, pos in current_path.items():
                        if pos >= cycle_start_depth:
                            in_team[cycle_student] = True
                continue

            visited[node] = True
            current_path[node] = depth

            next_node = choices[node]
            q.append((next_node, depth + 1))

    print(no_team_count)