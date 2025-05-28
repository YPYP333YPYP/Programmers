N, M = map(int, input().split())


numbers = [x for x in range(1,N+1)]


def gen(arr,r):
    result = []

    def dfs(s, path):
        if len(path) == r:
            result.append(path[:])
            return

        for i in range(s, len(arr)):
            path.append(arr[i])
            dfs(i+1, path)
            path.pop()

    dfs(0,[])
    return result

result = gen(numbers,M)

for v in result:
    print(*v, sep=" ")