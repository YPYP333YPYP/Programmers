from collections import deque

N = int(input())

numbers = [x for x in range(1,N+1)]

q = deque(numbers)


if N == 1:
    print(numbers[0])

elif N == 2:
    print(numbers[1])
    
else:
    while len(q) != 1:
        x = q.popleft()
        y = q.popleft()
        q.append(y)

    print(q[0])