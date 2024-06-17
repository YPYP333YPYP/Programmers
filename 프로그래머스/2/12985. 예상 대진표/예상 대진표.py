def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def solution(n,a,b):
    answer = 0
    slist = [ x for x in range(1,n+1)]
    cnt = 0
    i = 2
    while i > 0:
        vlist = list_chunk(slist, i)
        for v in vlist:
            if a in v and b in v:
                i = 0
            
        cnt +=1
        i *=2
    answer = cnt   
    return answer