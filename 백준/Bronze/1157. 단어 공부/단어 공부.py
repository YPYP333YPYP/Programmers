string = list(input())


sdict = dict()

for v in string:
    v = v.upper()
    if v in sdict.keys():
        sdict[v] += 1
    else:
        sdict[v] = 1


sdict = sorted(sdict.items(), key=lambda x: x[1], reverse=True)


if len(sdict) > 1:
    if sdict[0][1] == sdict[1][1]:
        print("?")
    else:
        print(sdict[0][0])
else:
    print(sdict[0][0])

