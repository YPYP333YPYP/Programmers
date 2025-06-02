from collections import deque

T = int(input())


def sol():
    N = int(input())

    stock = list(map(int, input().split()))

    stock.reverse()

    high = stock[0]

    buy = []
    result = 0
    for i in range(1,len(stock)):
        if high > stock[i]:
            buy.append(stock[i])
        elif high < stock[i]:
            result += sum([high-x for x in buy])
            buy = []
            high = stock[i]

        if i == len(stock)-1:
            result += sum([high - x for x in buy])

    return result

for _ in range(T):
    print(sol())
