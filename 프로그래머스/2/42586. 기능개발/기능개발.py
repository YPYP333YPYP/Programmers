from math import ceil
from collections import deque
def solution(progresses, speeds):
    answer = []
    slist= []
    for v in range(len(speeds)):
        slist.append(100 - progresses[v])
        slist[v] = ceil(slist[v] / speeds[v])
    print(slist)
    cnt = 1
    mx = 0
    for v in range(len(slist)):
        if v == 0:
            mx = slist[v]
        else:
            if mx >= slist[v]:
                cnt +=1   
            else :
                mx = slist[v]
                answer.append(cnt)
                cnt = 1
        if v == len(slist)-1:
                answer.append(cnt)
    return answer