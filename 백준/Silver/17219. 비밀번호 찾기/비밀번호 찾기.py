N,M = map(int, input().split())

ndict = dict()
for _ in range(N):
    key, val = map(str, input().split())
    ndict[key] = val

result = []
for _ in range(M):
    key = input()
    if key in ndict:
        result.append(ndict[key])


for v in result:
    print(v)