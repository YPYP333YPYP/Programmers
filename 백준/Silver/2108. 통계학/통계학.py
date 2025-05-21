
N = int(input())

numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)


avg = int(round(sum(numbers) / len(numbers),0))

middle = 0
numbers.sort()
if N > 1:
    middle = numbers[int((N-1)/2)]
else:
    middle = numbers[0]

sdict = { x : 0 for x in numbers }

for v in numbers:
    if v in sdict.keys():
        sdict[v] += 1


most_common = sorted(sdict.items())
most_common.sort(key=lambda x:x[1], reverse=True)

mx = most_common[0]
most_common_list = []
for v in most_common:
    if v[1] == mx[1]:
        most_common_list.append(v[0])

mc = 0
if len(most_common_list) == 1:
    mc = most_common_list[0]
else:
    most_common_list.sort()
    mc = most_common_list[1]

rg = 0
if N == 1:
    rg = 0
else:
    mx = max(numbers)
    mn = min(numbers)
    rg = mx - mn

print(avg)
print(middle)
print(mc)
print(rg)
