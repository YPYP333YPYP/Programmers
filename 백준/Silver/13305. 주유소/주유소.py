N = int(input())

d = list(map(int, input().split()))
node = list(map(int, input().split()))


result = 0

money = 0
for i in range(N-1):
    if i == 0:
        money = node[i]
    else:
        if money > node[i]:
            money = node[i]

    result += money * d[i]

print(result)

