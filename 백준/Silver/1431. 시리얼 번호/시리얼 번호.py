N = int(input())

serial = []
numbers = [str(x) for x in range(10)]

for _ in range(N):
    serial.append(str(input()))

info = []
for v in serial:
    length = len(v)
    num_sum = 0
    for k in v:
        if k in numbers:
            num_sum += int(k)
    info.append([v,length,num_sum])

result = sorted(info, key=lambda x:(x[1],x[2],x[0]))

for v in result:
    print(v[0])

