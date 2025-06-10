def solve():
    T = int(input())
    
    for _ in range(T):
        W = input().strip()
        K = int(input())
        
        def sliding_window_t3(string):
            min_result = float('inf')
            
            for target_char in set(string):  # 각 문자별로 따로 처리
                window = []
                count = 0
                
                for right in range(len(string)):
                    s = string[right]
                    window.append(s)
                    
                    # target_char인 경우에만 카운트
                    if s == target_char:
                        count += 1
                    
                    # target_char가 정확히 K개가 되면
                    while count == K:
                        min_result = min(min_result, len(window))
                        
                        # 왼쪽에서 하나씩 제거
                        p = window.pop(0)
                        if p == target_char:
                            count -= 1
            
            return min_result if min_result != float('inf') else -1

        def sliding_window_t4(string):
            max_result = -1
            
            for target_char in set(string):  # 각 문자별로 따로 처리
                window = []
                count = 0
                
                for right in range(len(string)):
                    s = string[right]
                    window.append(s)
                    
                    # target_char인 경우에만 카운트
                    if s == target_char:
                        count += 1
                    
                    # target_char가 정확히 K개가 되면
                    while count == K:
                        # 첫 번째와 마지막이 target_char인지 확인 (자동으로 만족됨)
                        if window[0] == window[-1] == target_char:
                            max_result = max(max_result, len(window))
                        
                        # 왼쪽에서 하나씩 제거
                        p = window.pop(0)
                        if p == target_char:
                            count -= 1
            
            return max_result

        result_3 = sliding_window_t3(W)
        result_4 = sliding_window_t4(W)
        
        if result_3 == -1:
            print(-1)
        else:
            print(result_3, result_4)

solve()