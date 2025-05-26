N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

result = []
stack = []
i = 1
j = 0

stack.append(i)
result.append("+")
flag = True

while True:
    if i == N:
        if len(stack) == 0:
            break
        else:
            if stack[-1] == numbers[j]:
                stack.pop(-1)
                j += 1
                result.append("-")
            else:
                flag = False
                break

    else:
        if len(stack) == 0:
            i += 1
            stack.append(i)
            result.append("+")
        else:
            if stack[-1] == numbers[j]:
                stack.pop(-1)
                j += 1
                result.append("-")
            else:
                i += 1
                stack.append(i)
                result.append("+")

if flag:
    for v in result:
        print(v)
else:
    print("NO")