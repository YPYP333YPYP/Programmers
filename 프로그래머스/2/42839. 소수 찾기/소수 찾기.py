import itertools

def is_prime(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2,x):
        if(x % i == 0):
            return False
    return True

def solution(numbers):
    answer = 0
    slist = []
    for i in range(1, len(numbers)+1):
        slist += list(itertools.permutations(numbers,i))
    stp = set()
    for v in slist:
        s = ""
        for x in v:
            s += x
            stp.add(int(s))
    for v in stp:
        if is_prime(v):
            answer+=1
    return answer