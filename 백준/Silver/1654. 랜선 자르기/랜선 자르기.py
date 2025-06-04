K, N = map(int, input().split())

lan = []

for _ in range(K):
    lan.append(int(input()))

def binary_search(arr, left, right):

    def get_cnt(val):
        cnt = 0
        for v in arr:
            cnt += v // val

        return cnt

    result = -1
    while left <= right:

        mid = (left+right)//2

        if get_cnt(mid) >= N:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

print(binary_search(lan, 1, max(lan)))
