n,d,k,c = map(int,input().split())

obj = []

for _ in range(n):
    obj.append(int(input()))


def two_pointer(arr,t):
    window = []
    result = -1

    for right in range(0, n+k):
        if right >= n:
            right = right - n
        window.append(arr[right])

        if len(window) > t:
            window.pop(0)

        tmp = len(set(window))
        if c not in window:
            tmp += 1
        result = max(tmp, result)

    return result


print(two_pointer(obj,k))
