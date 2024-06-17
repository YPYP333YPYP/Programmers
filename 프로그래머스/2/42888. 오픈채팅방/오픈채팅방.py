def solution(record):
    answer = []
    sdict = {}
    result = []
    for v in record:
        slist = v.split(' ')
        if slist[0] == "Enter":
            sdict[slist[1]] = slist[2]
            sstr = slist[1]+"님이 들어왔습니다."
            result.append(sstr)
        if slist[0] == "Leave":
            sstr = slist[1]+"님이 나갔습니다."
            result.append(sstr)
        if slist[0] == "Change":
            sdict.update({slist[1]: slist[2]})
    
    for v in result:
        tmp = v.split('님')
        if tmp[0] in sdict:
            sstr = sdict[tmp[0]] +"님" + tmp[1]
            answer.append(sstr)
            
    return answer