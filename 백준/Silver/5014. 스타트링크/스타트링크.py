from collections import deque
f, s, g, u, d = map(int, input().split())

def bfs(start, target, up, down):
    visited = [False] * (f+1)
    visited[start] = True
    
    q = deque()
    q.append((start, 0))
    
    while q:
        loc, button = q.popleft()
        
        if loc == target:
            return button
        
        for next_pos in [loc+up, loc-down]:
            if 1 <= next_pos <= f and not visited[next_pos]:
                q.append((next_pos, button+1))
                visited[next_pos] = True
    return -1

result = bfs(s, g, u, d)
if result == -1:
    print("use the stairs")
else:
    print(result)