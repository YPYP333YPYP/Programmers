N, money = map(int, input().split())

coin = []

for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

result = 0

for v in coin:
    if v > money:
        continue
    else:
        cnt = money // v
        money = money % v
        result += cnt

    if money == 0:
        break

print(result)