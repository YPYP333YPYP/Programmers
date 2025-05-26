T = int(input())

def sol():
    N = int(input())

    sdict = dict()
    for _ in range(N):
        item, type = input().split()
        if type in sdict:
            sdict[type].append(item)
        else:
            sdict[type] = [item]

    result = 1
    for v in sdict:
        result *= (len(sdict[v]) + 1)

    return result - 1

for _ in range(T):
    result = sol()
    print(result)