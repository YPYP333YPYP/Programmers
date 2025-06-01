N, M = map(int, input().split())

trees = list(map(int, input().split()))

def binary_search(tree, left, right):
    def condition(t, t_length):
        cut = sum(max(0, x - t_length) for x in t)
        if cut >= M:
            return True
        else:
            return False

    result = -1
    while left <= right:
        mid = (left + right) // 2
        if condition(trees, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

print(binary_search(trees,0,max(trees)))