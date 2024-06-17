def solution(s):
    answer = 0
    strings = s
    i = 0
    x_cnt = 1
    x_not_cnt = 0
    while True:
        print(i)
        if len(strings) == 1:
            answer+=1
            break
        elif len(strings) == 0:
            break
        elif len(strings) -1 == i:
            answer+=1
            break
            
        if strings[0] == strings[i+1]:
            x_cnt += 1
        else:
            x_not_cnt +=1
        i += 1
        if x_cnt == x_not_cnt:
            strings = strings[i+1:]
            x_cnt = 1
            x_not_cnt = 0
            answer +=1
            i = 0 
    return answer