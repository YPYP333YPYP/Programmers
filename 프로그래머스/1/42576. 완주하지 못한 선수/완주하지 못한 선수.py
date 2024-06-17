from collections import Counter

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    ln = len(participant)-1
    i = 0
    
    while True:
        if ln == i:
            answer = participant[i]
            break
        elif participant[i] != completion[i]:
            answer = participant[i]
            break
        i+=1
    return answer