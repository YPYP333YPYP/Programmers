import itertools


N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
slist = list(numbers)

plist = list(itertools.permutations(slist,M))
plist = set(plist)
plist = list(plist)
plist.sort()

for i in range(len(plist)):
    string = ""
    for v in plist[i]:
        string += str(v) + " "
    print(string, sep='')