N, M = map(int, input().split())

numbers = list(map(int, input().split()))


arr = [0] + numbers
s = [0] * (N+1)

for i in range(1, N+1):
    s[i] = s[i-1] + arr[i]

for _ in range(M):
    x,y = map(int, input().split())
    print(s[y] - s[x-1])