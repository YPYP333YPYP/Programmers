import heapq

def solution(n, works):
    heap = [-x for x in works] 
    heapq.heapify(heap)

    for _ in range(n):
        if not heap: 
            break
        biggest = heapq.heappop(heap) 
        biggest += 1  
        heapq.heappush(heap, biggest)  

    return sum(x**2 for x in heap if x < 0)  