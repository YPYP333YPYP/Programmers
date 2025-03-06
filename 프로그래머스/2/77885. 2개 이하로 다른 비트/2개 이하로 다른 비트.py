def solution(numbers):
    answer = []
    
    for v in numbers:
        # 짝수인 경우 -> 바로 다음에 오는 수
        if v%2 == 0:
            answer.append(v+1)
    
        # 홀수인 경우 -> 다른 비트의 개수는 최대 2개
        # 홀수이기에 마지막 자리 (2^0)는 반드시 1
        # 마지막 자리(1)과 그 다음 자리를 0으로 변환 <- 다른 비트는 최대 2개 임으로 
        else:
            val = '0' + bin(v)[2:]
            idx = val.rfind('0')
            val = list(val)
            
            val[idx] = '1'
            val[idx+1] = '0'
            
            val = ''.join(val)
            result = int(val,2)
            answer.append(result)
        
    return answer