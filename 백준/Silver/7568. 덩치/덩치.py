N = int(input())

p = []

for _ in range(N):
    p.append(list(map(int, input().split())))

result = []

for i in range(N):
    x,y = p[i][0], p[i][1]
    k = 1
    for j in range(N):
        if j == i:
            continue
        else:
            a,b = p[j][0], p[j][1]
            if a > x and b > y:
                k += 1

    result.append(k)

print(*result, sep=" ")
