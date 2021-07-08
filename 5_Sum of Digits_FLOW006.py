# cook your dish here

def find_sum_of_digits(n):
    
    s = 0
    
    while n > 0:
        r = n%10
        s += r
        n //= 10
    return s
    
T = int(input())

for i in range(T):
    print(find_sum_of_digits(int(input())))
    