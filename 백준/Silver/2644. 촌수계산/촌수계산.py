N = int(input())

a, b = map(int, input().split())

V = int(input())

def dfs(start, target, depth):
    if start == target:  
        return depth
    
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            result = dfs(i, target, depth + 1)
            if result != -1:  
                return result
    
    return -1  
            

graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)

for _ in range(V):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(dfs(a, b, 0))
    