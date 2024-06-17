def solution(numbers, target):
    answer = 0
    def backtrack(index, total):
        nonlocal answer
        if index == len(numbers):
            if total == target:
                answer += 1
            return
        
        backtrack(index + 1, total + numbers[index])
        backtrack(index + 1, total - numbers[index])
    
    backtrack(0, 0)
    return answer