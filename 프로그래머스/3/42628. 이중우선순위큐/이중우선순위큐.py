def solution(operations):
    answer = []
    stack = []
    for v in operations:
        tmp = v.split(" ")
        if tmp[0] == "I":
            stack.append(int(tmp[1]))
        else:
            if stack :
                if int(tmp[1]) == 1:
                    stack.remove(max(stack))
                else:
                    stack.remove(min(stack))
    if stack:
        answer = [max(stack), min(stack)]
    else:
        answer = [0,0]
    return answer