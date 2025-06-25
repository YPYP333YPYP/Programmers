n, k = map(int, input().split())

value = list(input())


result = 0
for i in range(len(value)):
    if value[i] == 'P':
        start = i-k
        end = i+k
        if start < 0:
            start = 0
        if end > len(value)-1:
            end = len(value)-1

        for j in range(start, end+1):
            if i == j:
                continue
            if value[j] == 'H':
                value[j] = "O"
                result +=1
                break

print(result)