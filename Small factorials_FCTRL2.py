def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

t = int(input())


for i in range(t):
    n = int(input())
    f = fact(n)
    print(f)