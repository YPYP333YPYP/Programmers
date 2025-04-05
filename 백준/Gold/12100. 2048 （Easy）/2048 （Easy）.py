n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

max_block = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def copy_board(board):
    return [row[:] for row in board]

def move(board, direction):
    new_board = copy_board(board)
    
    merged = [[False] * n for _ in range(n)]
    
    if direction == 0:
        for i in range(1, n):
            for j in range(n):
                if new_board[i][j] == 0:
                    continue
                    
                x, y = i, j
                val = new_board[x][y]
                new_board[x][y] = 0
                
                while x > 0 and new_board[x-1][y] == 0:
                    x -= 1
                
                if x > 0 and new_board[x-1][y] == val and not merged[x-1][y]:
                    new_board[x-1][y] *= 2
                    merged[x-1][y] = True
                else:
                    new_board[x][y] = val
    
    elif direction == 1:
        for j in range(n-2, -1, -1):
            for i in range(n):
                if new_board[i][j] == 0:
                    continue
                    
                x, y = i, j
                val = new_board[x][y]
                new_board[x][y] = 0
                
                while y < n-1 and new_board[x][y+1] == 0:
                    y += 1
                
                if y < n-1 and new_board[x][y+1] == val and not merged[x][y+1]:
                    new_board[x][y+1] *= 2
                    merged[x][y+1] = True
                else:
                    new_board[x][y] = val
    
    elif direction == 2:
        for i in range(n-2, -1, -1):
            for j in range(n):
                if new_board[i][j] == 0:
                    continue
                    
                x, y = i, j
                val = new_board[x][y]
                new_board[x][y] = 0
                
                while x < n-1 and new_board[x+1][y] == 0:
                    x += 1
                
                if x < n-1 and new_board[x+1][y] == val and not merged[x+1][y]:
                    new_board[x+1][y] *= 2
                    merged[x+1][y] = True
                else:
                    new_board[x][y] = val
    
    elif direction == 3:
        for j in range(1, n):
            for i in range(n):
                if new_board[i][j] == 0:
                    continue
                    
                x, y = i, j
                val = new_board[x][y]
                new_board[x][y] = 0
                
                while y > 0 and new_board[x][y-1] == 0:
                    y -= 1
                
                if y > 0 and new_board[x][y-1] == val and not merged[x][y-1]:
                    new_board[x][y-1] *= 2
                    merged[x][y-1] = True
                else:
                    new_board[x][y] = val
    
    return new_board

def find_max(board):
    return max(max(row) for row in board)

def dfs(board, count):
    global max_block
    
    if count == 5:
        max_block = max(max_block, find_max(board))
        return
    
    for direction in range(4):
        new_board = move(board, direction)
        
        if new_board != board:
            dfs(new_board, count + 1)
        else:
            max_block = max(max_block, find_max(board))

dfs(board, 0)

print(max_block)