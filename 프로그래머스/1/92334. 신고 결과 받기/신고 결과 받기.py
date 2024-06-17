def solution(id_list, report, k):
    answer = []
    sdict = {}
    report_dict = {}
    mail_result = [0] * len(id_list)
    
    for i in range(len(report)):
        sdict[report[i]] = i
    
    for v in sdict:
        tmp = v.split(" ")
        if tmp[1] in report_dict:
            val = report_dict[tmp[1]]
            val+=1
            report_dict[tmp[1]] = val
        else:
            report_dict[tmp[1]] = 1
        
    for v in sdict:
        tmp = v.split(" ")
        if tmp[1] in report_dict and report_dict[tmp[1]] >= k:
            idx = id_list.index(tmp[0])
            mail_result[idx] +=1
   
    return mail_result