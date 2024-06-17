def solution(s):
    answer = 0
    
    
    for i in range(len(s)):
        stack = []
        for v in range(len(s)):
            if len(stack) == 0:
                stack.append(s[v])
            else:
                if s[v] == "}" and stack[-1] == "{":
                    stack.pop()
                elif s[v] == "]" and stack[-1] == "[":
                    stack.pop()
                elif s[v] == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(s[v])
        
        if len(stack) == 0:
            answer+=1
        s = s[1:] + s[:1]

    return answer