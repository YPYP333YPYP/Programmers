def solution(data, ext, val_ext, sort_by):
    type_list = ["code","date","maximum","remain"]
    
    index = type_list.index(ext)
    
    export = []
    for v in data:
        if v[index] < val_ext:
            export.append(v)
    sort_index = type_list.index(sort_by)
    export.sort(key= lambda x:x[sort_index])
    answer = export
    
    
    return answer