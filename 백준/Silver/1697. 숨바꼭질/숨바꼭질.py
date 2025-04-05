from collections import deque

n, k = map(int, input().split())
    
def bfs(n, k):
    q = deque()
    q.append((n, 0))
    
    max_pos = 100000
    visited = [False] * (max_pos+1)
    
    visited[n] = True
    
    while q:
        pos, time = q.popleft()
        
        if pos == k:
            return time
        
        for next_pos in [pos-1, pos+1, pos*2]:
            if 0<= next_pos <= max_pos and not visited[next_pos]:
                q.append((next_pos, time + 1))
                visited[next_pos] = True
print(bfs(n,k))