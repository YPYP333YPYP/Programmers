def solution(N, L, board):
    answer = 0
    
    # 길이 지나갈 수 있는지 확인하는 함수
    def check_path(path):
        used = [False] * N  # 경사로 설치 여부 기록
        
        for i in range(N-1):
            # 높이 차이 계산
            diff = path[i+1] - path[i]
            
            # 높이 차이가 2 이상이면 지나갈 수 없음
            if abs(diff) > 1:
                return False
            
            # 다음 칸이 1 높으면 현재 위치부터 왼쪽으로 경사로 설치
            if diff == 1:
                for j in range(L):
                    # 범위를 벗어나거나, 이미 경사로가 있거나, 높이가 다르면 실패
                    if i-j < 0 or used[i-j] or path[i-j] != path[i]:
                        return False
                    used[i-j] = True  # 경사로 설치 표시
            
            # 다음 칸이 1 낮으면 다음 위치부터 오른쪽으로 경사로 설치
            elif diff == -1:
                for j in range(L):
                    # 범위를 벗어나거나, 이미 경사로가 있거나, 높이가 다르면 실패
                    if i+1+j >= N or used[i+1+j] or path[i+1+j] != path[i+1]:
                        return False
                    used[i+1+j] = True  # 경사로 설치 표시
        
        return True
    
    # 모든 행 확인
    for i in range(N):
        row = board[i]
        if check_path(row):
            answer += 1
    
    # 모든 열 확인
    for j in range(N):
        col = [board[i][j] for i in range(N)]
        if check_path(col):
            answer += 1
    
    return answer

N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

print(solution(N, L, board))