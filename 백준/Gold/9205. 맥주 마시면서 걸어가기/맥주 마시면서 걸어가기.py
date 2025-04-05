from collections import deque

def can_reach_festival():
    n = int(input())  
    
    locations = []
    for _ in range(n + 2):
        x, y = map(int, input().split())
        locations.append((x, y))
    
    home = locations[0]
    festival = locations[n + 1]
    stores = locations[1:n+1]
    
    queue = deque([home])
    visited = set([home])
    
    while queue:
        current_x, current_y = queue.popleft()
        
        dist_to_festival = abs(current_x - festival[0]) + abs(current_y - festival[1])
        if dist_to_festival <= 1000:  
            return "happy"
        
        for store in stores:
            if store not in visited:
                store_x, store_y = store
                distance = abs(current_x - store_x) + abs(current_y - store_y)
                
                if distance <= 1000:
                    queue.append(store)
                    visited.add(store)
    
    return "sad"

t = int(input())

for _ in range(t):
    print(can_reach_festival())