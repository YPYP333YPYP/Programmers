N = int(input())

p = [[False] * 100 for _ in range(100)]


for _ in range(N):
    x,y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            if not p[y+i][x+j]:
                p[y+i][x+j] = True

s = 0
for i in range(100):
    for j in range(100):
        if p[i][j]:
            s += 1

print(s)