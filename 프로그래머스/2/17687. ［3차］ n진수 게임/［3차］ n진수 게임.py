def convert(number, k):
    answer = ''
    if number == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"

    while number > 0:
        remainder = number % k
        answer += hex_chars[remainder]
        number //= k

    return answer[::-1]


def solution(n, t, m, p):
    answer = ''
    i = 0
    while True:
        if len(answer) >= t*m :
            break
        word = convert(i,n)
        answer += word
        i+=1
    s = ''
    i = p-1
    while True:
        if len(s) == t:
            break
        s += answer[i]
        i += m
        
    return s