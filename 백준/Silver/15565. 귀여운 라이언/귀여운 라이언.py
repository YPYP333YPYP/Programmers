N, K = map(int, input().split())

doll = list(map(int, input().split()))

def two_pointer(arr, k):
    left = 0
    result = float("inf")

    cnt = 0
    for right in range(len(arr)):
        if arr[right] == 1:
            cnt +=1

        while cnt >= k:
            result = min(result, right - left+1)

            if arr[left] == 1:
                cnt -= 1

            left += 1

    return result if result < float("inf") else -1


print(two_pointer(doll,K))