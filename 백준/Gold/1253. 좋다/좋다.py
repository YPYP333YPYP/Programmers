import sys

def solution():
    # 입력 받기
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    
    # 배열 정렬
    numbers.sort()
    
    good_count = 0
    
    # 모든 수에 대해 검사
    for i in range(N):
        target = numbers[i]
        
        # 투포인터로 합이 target인 두 수 찾기
        left, right = 0, N - 1
        
        while left < right:
            # 자기 자신은 포함할 수 없음
            if left == i:
                left += 1
                continue
            if right == i:
                right -= 1
                continue
            
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                good_count += 1
                break
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    print(good_count)

solution()