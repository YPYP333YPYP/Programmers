"""
1 -> 1
2 ~ 7 (6개) -> 2
8 ~ 19 (12개) -> 3
20  ~ 37 (18개) -> 4
38 ~ 61 (24개) -> 5
"""

n = int(input())
x = 1
cnt = 1

if n == 1:
    print(1)
else:
    while n > x:
        x += 6*cnt
        cnt += 1
    print(cnt)