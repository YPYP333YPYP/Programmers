import sys
input = sys.stdin.readline

s = set()

for _ in range(int(input())):
    x = input().rstrip().split()			
    if len(x) > 1:						
        x[1] = int(x[1])				

    if x[0] == 'add':					
        s.add(x[1])						
    elif x[0] == 'remove' and x[1] in s:	
        s.remove(x[1])					
    elif x[0] == 'check':					
        print(1 if x[1] in s else 0)	
    elif x[0] == 'toggle':				
        if x[1] in s:					
            s.remove(x[1])
        else:								
            s.add(x[1])
    elif x[0] == 'all':						
        s = set(range(1, 21))				
    elif x[0] == 'empty':					
        s.clear()	