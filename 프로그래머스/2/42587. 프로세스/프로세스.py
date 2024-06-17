def solution(priorities, location):
    answer = 0
    q = []
    
    for i in range(len(priorities)):
        for i in range(len(priorities)):
            mx = max(priorities)
            if mx == priorities[i]:
                q.append(i)
                priorities[i] = 0
            if len(q) == len(priorities):
                break
        if len(q) == len(priorities):
            break
    
    
    answer = q.index(location) + 1
    
    
    
    
    return answer