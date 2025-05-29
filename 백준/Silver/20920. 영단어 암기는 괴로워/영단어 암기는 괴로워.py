N, M = map(int, input().split())

wdict = dict()
for _ in range(N):
    word = input()
    if len(word) < M:
        continue

    if word not in wdict:
        wdict[word] = [1,len(word)]
    else:
        a,b = wdict[word]
        wdict[word] = [a+1,b]

wlist = []
for v in wdict:
    a,b = wdict[v]
    wlist.append([a,b,v])


wlist.sort(key=lambda x: (-x[0],-x[1],x[2]))

for v in wlist:
    print(v[2])


