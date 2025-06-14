N = int(input())

status = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    status.append(tmp)


visited = [False] * N
result = float('inf')

def dfs(n, idx):
    global result

    if n == N//2:

        team_s = 0
        team_l = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team_s += status[i][j]
                elif not visited[i] and not visited[j]:
                    team_l += status[i][j]

        result = min(result, abs(team_s - team_l))
        return
    else:
        for i in range(idx,N):
            if not visited[i]:
                visited[i] = True
                dfs(n+1, i+1)
                visited[i] = False


dfs(0,0)
print(result)