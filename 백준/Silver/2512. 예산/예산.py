N = int(input())
bg = list(map(int, input().split()))
M = int(input())

bg.sort()


def binary_search(arr,left,right):

    def condition(array,val):
        s = 0
        for v in array:
            if v >= val:
                s += val
            else:
                s += v

        return s

    result = 0
    while left <= right:
        mid = (left + right) // 2
        if condition(arr,mid) <= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

print(binary_search(bg, 0, max(bg)))