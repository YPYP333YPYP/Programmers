n, m = map(int, input().split())  # n: 도시 크기, m: 남길 치킨집 수
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 집과 치킨집 위치 찾기
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:  # 집
            houses.append((i, j))
        elif city[i][j] == 2:  # 치킨집
            chickens.append((i, j))

# 치킨 거리 계산 함수
def chicken_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

# 도시의 치킨 거리 계산
def city_chicken_distance(selected_chickens):
    total_distance = 0
    for house in houses:
        # 각 집에서 가장 가까운 치킨집까지의 거리 계산
        min_dist = float('inf')
        for chicken in selected_chickens:
            dist = chicken_distance(house, chicken)
            min_dist = min(min_dist, dist)
        total_distance += min_dist
    return total_distance

# 백트래킹 함수
def backtracking(start, depth):
    global min_city_distance
    
    # m개의 치킨집을 모두 선택했으면 도시의 치킨 거리 계산
    if depth == m:
        distance = city_chicken_distance(selected)
        min_city_distance = min(min_city_distance, distance)
        return
    
    # 치킨집 선택
    for i in range(start, len(chickens)):
        selected[depth] = chickens[i]
        backtracking(i + 1, depth + 1)

min_city_distance = float('inf')
selected = [0] * m  # 선택된 치킨집을 저장할 배열

backtracking(0, 0)

print(min_city_distance)