import itertools


def solution(k, dungeons):
    answer = -1
    per = list(itertools.permutations(dungeons, len(dungeons)))
    
    for v in per:
        cnt = 0
        p = k
        for x in v:
            if x[0] <= p:
                p -= x[1]
                cnt+=1
            else:
                break
        if cnt > answer:
            answer = cnt
    
    return answer