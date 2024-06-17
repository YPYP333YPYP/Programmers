def solution(board, moves):
    answer = 0
    stack = []
    board_v2 = [[] for _ in range(len(board))]
    for v in range(len(board)-1, -1, -1):
        for p in range(len(board)):
            board_v2[p].append(board[v][p])
    
    for v in moves:
        while True:
            if len(board_v2[v-1]) == 0:
                tmp = 0
                break
            else:
                tmp = board_v2[v-1].pop()
                if tmp != 0:
                    break
        if tmp != 0:        
            if len(stack) == 0:
                stack.append(tmp)

            else:
                if stack[-1] == tmp:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(tmp)
            
        
    return answer