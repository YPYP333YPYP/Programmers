import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    
    while True:
        smallest = heapq.heappop(heap)
        if smallest >= K:
            break
        second = heapq.heappop(heap)
        if len(heap) == 0 and (smallest + (second * 2)) < K:
            return -1
        val = smallest + second * 2
        heapq.heappush(heap,val)
        answer +=1
    return answer