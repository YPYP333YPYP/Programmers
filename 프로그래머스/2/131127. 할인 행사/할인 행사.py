def solution(want, number, discount):
    answer = 0
    slist = []
    for v in range(len(want)):
        for i in range(number[v]):
            slist.append(want[v])
    
    slist.sort()
    for i in range(len(discount)):
        dlist = discount[i:i+10]
        dlist.sort()
        if dlist == slist:
            answer+=1
    
    return answer