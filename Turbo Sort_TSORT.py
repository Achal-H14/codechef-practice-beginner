# https://www.codechef.com/problems/TSORT

t = int(input())

arr = list()

for i in range(t):
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i)
    