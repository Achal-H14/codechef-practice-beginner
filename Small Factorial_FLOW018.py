# https://www.codechef.com/problems/FLOW018

def find_fact(n):
    if n != 0:
        if n == 1 :
            return 1
        else:
            return n*find_fact(n-1)
    else:
        return 1
        
t = int(input())

for _ in range(t):
    n = int(input())
    
    ans = find_fact(n)
    print(ans)