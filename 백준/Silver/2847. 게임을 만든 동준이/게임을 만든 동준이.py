N = int(input())

level = []
for _ in range(N):
    level.append(int(input()))

level.reverse()

now = level[0]
result = 0

for i in range(1,len(level)):
    if now <= level[i]:
        now = now - 1
        result += level[i] - now
    else:
        now = level[i]

print(result)