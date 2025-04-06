N, M = map(int, input().split())

# 결과를 저장할 배열
result = [0] * M

# 방문 여부를 체크하는 배열
visited = [False] * (N + 1)

def backtrack(depth):
    # 깊이가 M이 되면 현재 수열 출력
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    # 1부터 N까지의 수에 대해 탐색
    for i in range(1, N + 1):
        # 아직 방문하지 않은 숫자라면
        if not visited[i]:
            # 현재 숫자를 선택하고 방문 표시
            result[depth] = i
            visited[i] = True
            
            # 다음 위치 탐색
            backtrack(depth + 1)
            
            # 백트래킹 - 방문 표시 해제
            visited[i] = False

# 백트래킹 시작
backtrack(0)