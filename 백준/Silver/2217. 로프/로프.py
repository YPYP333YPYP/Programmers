N = int(input())

rope = []
for _ in range(N):
    rope.append(int(input()))


rope.sort(reverse=True)

approve = []
result = 0
for v in rope:

    approve.append(v)

    k = len(approve)
    w = k * v

    if v >= w/k:
        result = max(result,w)
        
print(result)