N,M = map(int, input().split())

ndict = dict()
for _ in range(N):
    val = input()
    ndict[val] = 1

cnt = 0
result = []
for _ in range(M):
    val = input()
    if val in ndict:
        cnt += 1
        result.append(val)

result.sort()

print(cnt)
for v in result:
    print(v)