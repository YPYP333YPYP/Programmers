from collections import Counter

def solution(weights):
    # 무게별 인원 수를 계산
    weight_counter = Counter(weights)
    answer = 0
    
    # 각 무게에 대해 짝꿍 찾기
    for weight, count in weight_counter.items():
        # 같은 무게인 경우 (nC2 조합으로 계산)
        if count > 1:
            answer += count * (count - 1) // 2
        
        # 다른 무게인 경우 (가능한 비율: 2:3, 2:4, 3:4)
        # 2:3 비율 (weight * 1.5)
        if weight * 3/2 in weight_counter:
            answer += count * weight_counter[weight * 3/2]
        
        # 2:4 비율 (weight * 2)
        if weight * 2 in weight_counter:
            answer += count * weight_counter[weight * 2]
        
        # 3:4 비율 (weight * 4/3)
        if weight * 4/3 in weight_counter:
            answer += count * weight_counter[weight * 4/3]
    
    return answer