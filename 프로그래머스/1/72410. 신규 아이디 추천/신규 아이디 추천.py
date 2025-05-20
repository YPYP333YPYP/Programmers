def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    alist = [chr(i) for i in range(ord('a'),ord('z')+1)]
    nlist = [str(x) for x in range(0,10)]
    elist = ["-","_","."]
    
    delete_list = alist + nlist + elist
    new_id = list(new_id)
    
    string = []
    for v in new_id:
        if v in delete_list:
            string.append(v)
    
    string_v2 = []
    for i in range(len(string)-1):
        if string[i] == string[i+1] == ".":
            continue
        else:
            string_v2.append(string[i])
    string_v2.append(string[-1])
    
    if string_v2[0] == ".":
        string_v2.pop(0)
    elif string_v2[-1] == ".":
        string_v2.pop(-1)
    
    if len(string_v2) == 0:
        string_v2 = "a"
    
    string_v2 = string_v2[:15]
    if string_v2[-1] == ".":
        string_v2.pop(-1)
    
    if len(string_v2) <= 2:
        while len(string_v2) != 3:
            string_v2 += string_v2[-1]
        string_v3 = ""
        for v in string_v2:
            string_v3 += v
        answer = string_v3
    elif len(string_v2) >= 3:
        string_v3 = ""
        for v in string_v2:
            string_v3 += v
        answer = string_v3
    
        
            
    
    return answer