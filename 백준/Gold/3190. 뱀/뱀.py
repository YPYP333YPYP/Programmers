from collections import deque


n = int(input())  
k = int(input())  
apple_positions = []
for _ in range(k):
    row, col = map(int, input().split())
    apple_positions.append((row, col))

l = int(input())  
direction_changes = {}
for _ in range(l):
    x, c = input().split()
    direction_changes[int(x)] = c

board = [[0] * (n+1) for _ in range(n+1)]
for apple in apple_positions:
    board[apple[0]][apple[1]] = 1  

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate():
    snake = deque([(1, 1)])  
    board[1][1] = 2  
    direction = 0  
    time = 0
    
    while True:
        time += 1
        head_x, head_y = snake[-1]
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]
        
        if nx < 1 or nx > n or ny < 1 or ny > n or (nx, ny) in snake:
            return time
        
        snake.append((nx, ny))
        
        if board[nx][ny] == 1:
            board[nx][ny] = 0  
        else:
            snake.popleft()
        
        if time in direction_changes:
            if direction_changes[time] == 'L':  
                direction = (direction - 1) % 4
            else:  
                direction = (direction + 1) % 4
    
print(simulate())