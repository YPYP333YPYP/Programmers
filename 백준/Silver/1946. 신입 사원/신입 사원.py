T = int(input())

def solution():
    N = int(input())

    p = []
    for _ in range(N):
        a,b = map(int,input().split())
        p.append((a,b))

    mn_list = sorted(p, key=lambda x: (x[0],x[1]))
    mn = mn_list[0]


    result = 1

    for v in mn_list:
        if mn[0] > v[0] or mn[1] > v[1]:
            result += 1
            mn = v

    print(result)

for _ in range(T):
    solution()