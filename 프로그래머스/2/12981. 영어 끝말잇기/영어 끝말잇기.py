def solution(n, words):
    answer = []
    
    for i in range(1, len(words)):
        if (words[i] in words[:i] or words[i-1][-1] != words[i][0]):
            answer.append((i%n)+1)
            answer.append((i//n)+1)
            break
    else:
        answer = [0,0]

    return answer