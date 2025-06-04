N, K = map(int, input().split())
numbers = list(map(int, input().split()))



sdict = dict()
def two_pointer(arr, k):
    left = 0
    result = 1
    sdict[arr[left]] = 1

    for right in range(1,len(arr)):
        if arr[right] in sdict:
            sdict[arr[right]] += 1
        else:
            sdict[arr[right]] = 1

        while sdict[arr[right]] > k:
            sdict[arr[left]] -= 1
            left += 1
        result = max(result, right-left + 1)
    return result

print(two_pointer(numbers, K))