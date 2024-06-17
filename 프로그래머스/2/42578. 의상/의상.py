def solution(clothes):
    answer = 1
    result = dict()
    for item, category in clothes:
        if category in result:
            result[category].append(item)
        else:
            result[category] = [item]
        
    for v in result:
        answer *= (len(result[v]) +1)
        
    return answer -1