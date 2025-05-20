def solution(wallpaper):
    answer = []
    
    graph = []
    file_y = []
    file_x = []
    for i,wall in enumerate(wallpaper):
        row = []
        for j,v in enumerate(wall):
            row.append(v)
            if v == "#":
                file_y.append(i)
                file_x.append(j)
    
        graph.append(row)
    file_x.sort()
    file_y.sort()
    answer = [file_y[0],file_x[0],file_y[-1]+1,file_x[-1]+1]
    
    return answer