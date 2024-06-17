from itertools import combinations
def solution(elements):
    answer = 0
    vset = set()
    l = len(elements)
    elements = elements*2
    for i in range(l):
        for v in range(l):
            vset.add(sum(elements[v:v+i+1]))
    answer = len(vset)
    return answer