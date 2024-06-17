def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
        
    
    return answer