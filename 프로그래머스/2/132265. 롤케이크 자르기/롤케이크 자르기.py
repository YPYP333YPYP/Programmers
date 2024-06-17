from collections import Counter 

def solution(topping):
    answer = 0
    old = Counter(topping) 
    young = set()  
        
    for i in topping:
        old[i] -= 1
        young.add(i)  
        
        if old[i] == 0:
            old.pop(i) 
        if len(old) == len(young): 
            answer += 1 
            
    return answer