def solution(survey, choices):
    answer = ''
    sdict = {"A":0,"N":0,"C":0,"F":0,"M":0,"J":0,"R":0,"T":0}
    score_list = [3,2,1,0,1,2,3]
    
    for i,v in enumerate(survey):
        left,right = v[0],v[1]
        index = choices[i] - 1
        if 0 <= index <= 2:
            sdict[left] += score_list[index]
        elif 4 <= index <= 6:
            sdict[right] += score_list[index]
    
    for x,y in [("R","T"),("C","F"),("J","M"),("A","N")]:
        if sdict[x] > sdict[y]:
            answer += x
        elif sdict[x] < sdict[y]:
            answer += y
        else:
            answer += x
        
    return answer