N = int(input())
A = list(map(int, input().split()))

M = int(input())
mlist = list(map(int, input().split()))

A.sort()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


for i in range(len(mlist)):
    print(binary_search(A, mlist[i]))