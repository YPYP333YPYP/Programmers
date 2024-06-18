import itertools

def solution(n, s):
    answer = []
    p1 = s // n
    p2 = s % n
    for i in range(n):
        if i >= n-p2:
            answer.append(p1+1)
        else:
            answer.append(p1)
    if p1 <= 0:
        return [-1]
    return answer