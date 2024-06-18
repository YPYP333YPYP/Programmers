def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    
    for v in skill_trees:
        stack = []
        flag = True
        for i in range(len(v)):
            if v[i] in skill:
                stack.append(v[i])
        for j in range(len(stack)):
            if stack[j] != skill[j]:
                flag = False
        if flag == True:
            answer +=1
            
 
    return answer