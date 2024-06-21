import functools

def solution(numbers):
    numbers = list(map(str, numbers))
    
    def compare(a, b):
        if a+b > b+a:
            return -1
        elif a+b < b+a:
            return 1
        else:
            return 0
    numbers.sort(key=functools.cmp_to_key(compare))
    
    answer = ''.join(numbers)
    
    return '0' if answer[0] == '0' else answer