n = int(input())
lst = []
result = 0

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

# 기둥을 x축 순으로 정렬
lst.sort()

# 가장 높은 기둥의 인덱스 찾기
max_height = 0
idx = 0
for i in range(n):
    if lst[i][1] > max_height:
        max_height = lst[i][1]
        idx = i

# 왼쪽부터 최고점까지 처리
height = lst[0][1]
for i in range(idx):
    if height < lst[i+1][1]:  # 다음 기둥이 더 높으면
        result += height * (lst[i+1][0] - lst[i][0])
        height = lst[i+1][1]  # 높이 갱신
    else:  # 현재 높이 유지
        result += height * (lst[i+1][0] - lst[i][0])

# 오른쪽부터 최고점까지 처리
height = lst[-1][1]
for i in range(n-1, idx, -1):
    if height < lst[i-1][1]:  # 이전 기둥이 더 높으면
        result += height * (lst[i][0] - lst[i-1][0])
        height = lst[i-1][1]  # 높이 갱신
    else:  # 현재 높이 유지
        result += height * (lst[i][0] - lst[i-1][0])

# 최고점 기둥의 면적 추가
result += max_height

print(result)