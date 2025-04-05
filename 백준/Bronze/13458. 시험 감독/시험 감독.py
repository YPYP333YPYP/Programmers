# 시험장의 개수
n = int(input())
# 시험장 별 인원 수
n_list = list(map(int, input().split()))
# 총감독관 용량, 부감독관 용량
m, k = map(int, input().split())
count = 0

for v in n_list:
    # 총 응시자 수 - 총 감독관 수
    now = v - m
    count += 1  # 각 시험장당 총감독관 1명
    
    # 필요한 부 감독관 수 계산
    if now > 0:  # 남은 학생이 있는 경우만 부감독관 필요
        tmp = (now + k - 1) // k 
        count += tmp
    
print(count)