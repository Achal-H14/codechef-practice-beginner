# https://www.codechef.com/problems/FLOW017

def find_second_larget(a):
    l = 0
    sl = 0
    
    for i in a:
        if i > sl:
            if i > l:
                sl = l
                l = i
            elif i < l:
                sl = i
                
    return sl
    
t = int(input())

for _ in range(t):
    arr = [int(x) for x in input().split()]
    ans = find_second_larget(arr.copy())
    print(ans)
    
    
    
    