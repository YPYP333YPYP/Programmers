r, c, k = map(int, input().split())
r, c = r-1, c-1  

A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

def R_operation(arr):
    max_len = 0
    new_arr = []
    
    for row in arr:
        counter = {}
        for num in row:
            if num == 0:
                continue
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        
        new_row = []
        for num, count in sorted_items:
            new_row.append(num)
            new_row.append(count)
        
        max_len = max(max_len, len(new_row))
        new_arr.append(new_row)
    
    for row in new_arr:
        if len(row) < max_len:
            row.extend([0] * (max_len - len(row)))
        
        if len(row) > 100:
            row = row[:100]
    
    return new_arr

def C_operation(arr):
    transposed = list(zip(*arr))
    transposed = [list(row) for row in transposed]
    
    result = R_operation(transposed)
    
    final = list(zip(*result))
    final = [list(row) for row in final]
    
    return final

time = 0
while time <= 100:
    if r < len(A) and c < len(A[0]) and A[r][c] == k:
        print(time)
        break
    
    if len(A) >= len(A[0]):  
        A = R_operation(A)
    else:
        A = C_operation(A)
    
    time += 1
else:
    print(-1) 