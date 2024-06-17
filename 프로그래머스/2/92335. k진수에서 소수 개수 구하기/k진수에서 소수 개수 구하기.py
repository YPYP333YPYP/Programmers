
def converter(n,k):
    digits = []
    while n:
        n, remainder = divmod(n,k)
        digits.append(str(remainder))
    digits.reverse()
    return ''.join(digits)

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def add_list(li):
    s = ""
    if len(li) == 0:
        return 0
    for v in li:
        s += v
    return int(s)

def solution(n, k):
    answer = 0
     
        
    number = converter(n,k)
    stack = []
    li = []
    for v in number:
        if v != "0":
            stack.append(v)
        else:
            li.append(add_list(stack))
            stack = []
    li.append(add_list(stack))
    
    for v in li:
        if is_prime(v):
            answer+=1
            
    return answer