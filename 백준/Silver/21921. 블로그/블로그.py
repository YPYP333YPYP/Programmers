n, x = map(int, input().split())

numbers = list(map(int, input().split()))

def sw(arr):
    if len(arr) < x:
        return []

    wn_sum = sum(arr[:x])
    result = [wn_sum]

    for i in range(x, len(arr)):
        wn_sum += arr[i] - arr[i-x]
        result.append(wn_sum)

    return result

result = sw(numbers)

mx = max(result)
if mx == 0:
    print("SAD")
else:
    cnt = result.count(mx)
    print(mx)
    print(cnt)