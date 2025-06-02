N = int(input())

numbers = [x for x in range(1, N+1)]

def two_pointer(arr,n):
    cr = 0
    left = 0
    cnt = 0

    for right in range(len(arr)):
        cr += arr[right]

        while cr >= n:
            if cr == n:
                cnt += 1
            cr -= arr[left]
            left += 1


    return cnt


print(two_pointer(numbers,N))
