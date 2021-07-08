# cook your dish here
x, bal = [float(x) for x in input().split()]

res = bal

if x + 0.5 <= bal:
    if x%5==0:
        res = bal - ( x + 0.5)
    
    
        
print("%.2f"%res)
        
    
    