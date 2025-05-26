N, C = map(int, input().split())

numbers = list(map(int, input().split()))

sdict = dict()
for i, v in enumerate(numbers):
    if v not in sdict:
        sdict[v] = [1, i]
    elif v in sdict:
        a,b = sdict[v][0], sdict[v][1]
        sdict[v] = [a+1,b]

tmp = []
for k in sdict.keys():
    a,b = sdict[k]
    tmp.append([k,a,b])

tmp.sort(key = lambda x:(x[1],-x[2]),reverse=True)

result = []
for v in tmp:
    number,cnt = v[0],v[1]
    for i in range(v[1]):
        result.append(number)

print(*result, sep=" ")