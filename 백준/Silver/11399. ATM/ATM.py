N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

result = list()
for i in range(len(numbers)):
    if i == 0:
        result.append(numbers[i])
    else:
        val = result[i-1] + numbers[i]
        result.append(val)


print(sum(result))