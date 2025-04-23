import sys  
input = sys.stdin.readline  
from collections import deque  

def bfs():  
    q = deque()  
    q.append((0, 0, 1))  
    visited[0][0] = 0  
    while q:  
        si, sj, cnt = q.popleft()  
        if (si, sj) == (N-1, M-1):  
            print(cnt)  
            return  
        for d in range(4):  
            ni, nj = si+di[d], sj+dj[d]  
            if in_range(ni,nj) and visited[si][sj] + arr[ni][nj] < visited[ni][nj]:  
                # 현재 좌표까지 부수고 온 벽 + 다음 좌표의 값 (벽이면 1, 빈 공간이면 0)이 현재 기록된 부순 벽의 개수보다 작다면  
                # q에 넣어주기                
                visited[ni][nj] = visited[si][sj] + arr[ni][nj]  
                q.append((ni, nj, cnt+1))  
    print(-1)  

def in_range(ni, nj):  
    if 0<=ni<N and 0<=nj<M:  
        return 1  
    return 0  

N, M, K = map(int, input().split())  

arr = [list(map(int, list(input().strip()))) for _ in range(N)]  
di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]  
# visited[i][j]는 현재 좌표까지 최단 거리로 오면서 부순 벽의 개수  
visited = [[K+1]*M for _ in range(N)]  
bfs()