def solution(s, skip, index):
    answer = ''
    alist = [chr(i) for i in range(97,123)]
    for v in s:
        i = 0 
        stack = []
        idx = alist.index(v)
        while len(stack) != index:
            idx += 1
            if idx >= 26:
                idx = idx - 26
            word = alist[idx]
            if word not in skip:
                stack.append(word)
        answer += stack[-1]
    return answer