def sol():
    N = int(input())

    numbers = list(map(int, input().split()))

    tmp_dict = dict()
    for v in numbers:
        if v in tmp_dict:
            tmp_dict[v] += 1
        else:
            tmp_dict[v] = 1

    sdict = dict()

    for v in tmp_dict:
        if tmp_dict[v] == 6:
            sdict[v] = []

    i = 1
    for v in numbers:
        if v in sdict:
            sdict[v].append(i)
            i += 1

    mn = (0, float('inf'), 0)
    for v in sdict:
        tmp = sdict[v]
        result = sum(tmp[:4])
        val_5 = tmp[4]

        if mn[1] > result:
            mn = (v, result, val_5)
        elif mn[1] == result:
            if val_5 < mn[2]:
                mn = (v, result, val_5)

    print(mn[0])


T = int(input())

for _ in range(T):
    sol()




