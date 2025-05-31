p, m = map(int, input().split())

waiting = []

for _ in range(p):
    level, people = input().split()
    level = int(level)
    if len(waiting) == 0:
        waiting.append([(int(level), people)])
    else:
        flag = False
        for v in waiting:
            c = int(v[0][0])
            if len(v) < m:
                if c - 10 <= level <= c + 10:
                    index = waiting.index(v)
                    waiting[index].append((int(level), people))
                    flag = True
                    break

        if not flag:
            waiting.append([(int(level), people)])

for v in waiting:
    v.sort(key=lambda x:x[1])
    if len(v) == m:
        print("Started!")
        for i in v:
            a,b = i
            print(f"{a} {b}")
    else:
        print("Waiting!")
        for i in v:
            a,b = i
            print(f"{a} {b}")
