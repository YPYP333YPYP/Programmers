def solution(s):
    answer = True
    stack = []
    for v in s:
        if len(stack) == 0 and v == ")":
            return False
        elif v == "(":
            stack.append(v)
        elif v == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
            
    if len(stack) == 0:
        asnwer = True
    else: 
        answer = False
    return answer
    
        
        

   