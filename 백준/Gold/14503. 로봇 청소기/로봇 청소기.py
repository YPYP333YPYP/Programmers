n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]  
dc = [0, 1, 0, -1]

cleaned = 0

cleaned_area = [row[:] for row in room]

while True:
    if cleaned_area[r][c] == 0:
        cleaned_area[r][c] = 2
        cleaned += 1
    
    has_unclean = False
    
    for i in range(4):
        nd = (d + 3) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        
        if 0 <= nr < n and 0 <= nc < m and cleaned_area[nr][nc] == 0:
            r, c, d = nr, nc, nd
            has_unclean = True
            break
        
        d = nd
    
    if not has_unclean:
        back_d = (d + 2) % 4
        nr = r + dr[back_d]
        nc = c + dc[back_d]
        
        if 0 <= nr < n and 0 <= nc < m and cleaned_area[nr][nc] != 1:
            r, c = nr, nc
        else:
            break

print(cleaned)