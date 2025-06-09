N = int(input())
base = str(input())
comp = []
l = len(base)

for _ in range(N-1):
    comp.append(input())

result = 0
for v in comp:
    if len(v) == l-1:  # 한 글자 제거
        base_temp = list(base)
        match = True
        for s in v:
            if s in base_temp:
                base_temp.remove(s)
            else:
                match = False
                break
        if match and len(base_temp) == 1:
            result += 1
            
    elif len(v) == l:  # 한 글자 교체
        base_temp = list(base)
        v_temp = list(v)
        diff = 0
        for s in v_temp[:]:
            if s in base_temp:
                base_temp.remove(s)
                v_temp.remove(s)
        if len(base_temp) <= 1 and len(v_temp) <= 1:
            result += 1
            
    elif len(v) == l+1:  # 한 글자 추가
        v_temp = list(v)
        match = True
        for s in base:
            if s in v_temp:
                v_temp.remove(s)
            else:
                match = False
                break
        if match and len(v_temp) == 1:
            result += 1

print(result)