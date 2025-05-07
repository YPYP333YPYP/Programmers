from collections import Counter

string = input()
string = string.upper()
counter = Counter(string)
counts = counter.most_common()

if len(counts) > 1:
    v1,v2 = counts[0], counts[1]
    if v1[1] == v2[1]:
        print("?")
    else:
        print(v1[0])
else:
    print(counts[0][0])