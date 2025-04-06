def rotate(gear, direction):
    if direction == 1:  # 시계 방향
        return gear[-1] + gear[:-1]
    else:  # 반시계 방향
        return gear[1:] + gear[0]

def solution():
    # 4개의 톱니바퀴 상태 입력 받기
    gears = []
    for _ in range(4):
        gears.append(input().strip())
    
    k = int(input())
    
    for _ in range(k):
        # 회전시킬 톱니바퀴 번호(1~4)와 방향(1: 시계, -1: 반시계) 입력 받기
        gear_num, direction = map(int, input().split())
        gear_num -= 1  # 0-based 인덱스로 변환
        
        rotate_directions = [0] * 4
        rotate_directions[gear_num] = direction
        
        # 오른쪽 톱니바퀴들 확인
        for i in range(gear_num, 3):
            # 현재 톱니바퀴의 3시 방향(인덱스 2)과 다음 톱니바퀴의 9시 방향(인덱스 6)이 다르면 회전
            if gears[i][2] != gears[i+1][6]:
                rotate_directions[i+1] = -rotate_directions[i]
            else:
                break
        
        # 왼쪽 톱니바퀴들 확인
        for i in range(gear_num, 0, -1):
            # 현재 톱니바퀴의 9시 방향(인덱스 6)과 이전 톱니바퀴의 3시 방향(인덱스 2)이 다르면 회전
            if gears[i][6] != gears[i-1][2]:
                rotate_directions[i-1] = -rotate_directions[i]
            else:
                break
        
        # 모든 톱니바퀴 회전
        for i in range(4):
            if rotate_directions[i] != 0:
                gears[i] = rotate(gears[i], rotate_directions[i])
    
    score = 0
    for i in range(4):
        if gears[i][0] == '1':  
            score += (1 << i) 
    
    return score

print(solution())