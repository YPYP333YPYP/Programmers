t = []

while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        t.append([a,b,c])


for v in t:
    v.sort()
    a,b,c = v
    if a+b <= c:
        print("Invalid")
    else:
        if a==b==c:
            print("Equilateral")
        elif a==b or a==c or b==c:
            print("Isosceles")
        else:
            print("Scalene")

