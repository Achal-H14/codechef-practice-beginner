# https://www.codechef.com/problems/FLOW007


t = int(input())
for _ in range(t):
    n = int(input())
    rev = 0
    while n>0:
        r = n % 10
        n //= 10
        rev = rev*10 + r
    print(rev)