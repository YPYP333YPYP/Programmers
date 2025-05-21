N = int(input())

numbers = list(map(int, input().split()))

sorted_numbers = sorted(set(numbers))
sdict = {}
for i,v in enumerate(sorted_numbers):
    sdict[v] = i

new_arr = []
for v in numbers:
    index = sdict[v]
    new_arr.append(index)

print(*new_arr, sep =" ")