from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]  # 로봇이 추가할 양분
nutrition = [[5] * N for _ in range(N)]  # 현재 양분 상태

# 각 좌표마다 나이별 나무 수를 저장
tree_count = [[{} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1  # 0-indexed로 변환
    y -= 1
    if z in tree_count[x][y]:
        tree_count[x][y][z] += 1
    else:
        tree_count[x][y][z] = 1

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# K년 동안 시뮬레이션
for _ in range(K):
    # 1. 봄 & 여름 (한 번에 처리)
    for x in range(N):
        for y in range(N):
            if not tree_count[x][y]:  # 나무가 없으면 패스
                continue
                
            next_trees = {}
            add_nutrition = 0
            
            # 나이 순으로 정렬된 키
            ages = sorted(tree_count[x][y].keys())
            
            for age in ages:
                count = tree_count[x][y][age]
                available = nutrition[x][y] // age  # 현재 양분으로 성장 가능한 나무 수
                
                if available >= count:  # 모든 나무가 성장 가능
                    nutrition[x][y] -= age * count
                    if age + 1 in next_trees:
                        next_trees[age + 1] += count
                    else:
                        next_trees[age + 1] = count
                else:  # 일부만 성장 가능
                    if available > 0:
                        nutrition[x][y] -= age * available
                        if age + 1 in next_trees:
                            next_trees[age + 1] += available
                        else:
                            next_trees[age + 1] = available
                    
                    # 여름: 죽은 나무는 즉시 양분으로 변환
                    add_nutrition += (count - available) * (age // 2)
            
            # 양분 추가 (여름)
            nutrition[x][y] += add_nutrition
            tree_count[x][y] = next_trees
    
    # 2. 가을 & 겨울
    breeding = [[0] * N for _ in range(N)]  # 번식할 나무 수 미리 계산
    
    # 가을: 번식할 5의 배수 나이 나무 찾기
    for x in range(N):
        for y in range(N):
            for age, count in tree_count[x][y].items():
                if age % 5 == 0:  # 5의 배수 나이인 나무만
                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            breeding[nx][ny] += count
    
    # 번식된 나무 추가 및 겨울 양분 추가
    for x in range(N):
        for y in range(N):
            # 번식된 나무 추가 (1살 나무)
            if breeding[x][y] > 0:
                if 1 in tree_count[x][y]:
                    tree_count[x][y][1] += breeding[x][y]
                else:
                    tree_count[x][y][1] = breeding[x][y]
            
            # 겨울: 양분 추가
            nutrition[x][y] += A[x][y]

# 살아남은 나무 수 계산
total_trees = 0
for x in range(N):
    for y in range(N):
        for count in tree_count[x][y].values():
            total_trees += count

print(total_trees)