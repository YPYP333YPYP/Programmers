def solution(board, h, w):
    answer = 0
    l = len(board)
    color = board[h][w]
    if 0 <= h-1 <= l-1:
        if board[h-1][w] == color:
            answer +=1 
    if 0 <= h+1 <= l-1:
        if board[h+1][w] == color:
            answer +=1          
    if 0 <= w-1 <= l-1:
        if board[h][w-1] == color:
            answer +=1 
    if 0 <= w+1 <= l-1:
        if board[h][w+1] == color:
            answer +=1          
    return answer